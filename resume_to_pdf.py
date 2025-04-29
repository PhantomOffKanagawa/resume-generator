import jinja2
import yaml
import subprocess
import os
import sys
import argparse

# Load resume details from a YAML file
def load_resume_details(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def escape_latex(s):
    if not isinstance(s, str):
        return s
    return (s.replace('\\', r'\textbackslash{}')
             .replace('&', r'\&')
             .replace('%', r'\%')
             .replace('$', r'\$')
             .replace('#', r'\#')
             .replace('_', r'\_')
             .replace('{', r'\{')
             .replace('}', r'\}')
             .replace('~', r'\textasciitilde{}')
             .replace('^', r'\textasciicircum{}'))

def escape_dict(d):
    if isinstance(d, dict):
        return {k: escape_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [escape_dict(i) for i in d]
    else:
        return escape_latex(d)

# Generate a LaTeX file from resume details
def render_latex_from_template(resume_data, template_path, tex_path, version=None):
    # Add version to resume data if provided
    if version:
        resume_data['version'] = version
    
    resume_data = escape_dict(resume_data)
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    template = jinja2.Template(template_content, block_start_string='{%', block_end_string='%}', variable_start_string='{{', variable_end_string='}}')
    latex_content = template.render(**resume_data)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(latex_content)

def latex_to_pdf(tex_path, output_dir=None):
    command = ["pdflatex", "-interaction=nonstopmode"]
    if output_dir:
        command += ["-output-directory", output_dir]
    command.append(tex_path)
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        pdf_path = tex_path.replace('.tex', '.pdf')
        if output_dir:
            pdf_path = os.path.join(output_dir, os.path.basename(pdf_path))
        pdf_path = os.path.abspath(pdf_path)
        print(f"Checking for PDF at: {pdf_path}")
        if os.path.exists(pdf_path):
            return pdf_path
        else:
            print("pdflatex ran but PDF was not found. Output:")
            print(result.stdout)
            print(result.stderr)
            return None
    except subprocess.CalledProcessError as e:
        print(f"pdflatex failed with error code {e.returncode}:")
        print(e.stdout)
        print(e.stderr)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate resume PDF from YAML data')
    parser.add_argument('--version', help='Version to include in the resume')
    args = parser.parse_args()
    
    yaml_path = 'resume.yaml'  # Ensure this file exists in the directory
    template_path = 'resume_template.tex'  # Ensure this file exists in the directory
    tex_path = 'resume.tex'  # Output LaTeX file
    output_dir = '.'

    resume_data = load_resume_details(yaml_path)
    render_latex_from_template(resume_data, template_path, tex_path, args.version)
    pdf_path = latex_to_pdf(tex_path, output_dir)
    print(f"PDF generated at: {pdf_path}")
