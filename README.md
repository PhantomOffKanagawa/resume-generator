# 📄 Resume Generator

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-GPLV3-green?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-blue?style=for-the-badge&logo=githubactions&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-blue?style=for-the-badge&logo=latex&logoColor=white)
![GitHub Release](https://img.shields.io/github/v/release/PhantomOffKanagawa/resume-generator?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/PhantomOffKanagawa/resume-generator?style=for-the-badge)
![GitHub Repo Size](https://img.shields.io/github/repo-size/PhantomOffKanagawa/resume-generator?style=for-the-badge)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-blue?style=for-the-badge&logo=github&logoColor=white)](https://phantomoffkanagawa.github.io/resume-generator/)
![Commits](https://img.shields.io/github/commit-activity/m/PhantomOffKanagawa/resume-generator?style=for-the-badge)

> **Generate beautiful, consistent resumes from YAML using LaTeX and Jinja2 templates.**

I got tired of manually tracking down 8 different places to update my resume, so I made this! This is a simple Python script that takes a YAML file with your resume data and generates a PDF using LaTeX. It also includes a GitHub Actions workflow to automatically build and release your resume on every push.

## ✨ Features

- 📝 **Edit your resume in YAML** – Quickly update even from the github site
- 🎨 **Customizable LaTeX template** for professional results
- ⚡ **One-command PDF generation** (`python resume_to_pdf.py`)
- 🤖 **GitHub Actions workflow** to auto-build and release your PDF on every push
- 🛠️ **Easy to extend** for your own sections and styling
- 📦 **Local support** – works locally as well as from github actions
- **Commit Based Actions** – Automatically build and release your resume on every push to `main`

>[!NOTE]
> Commits can be marked with `[skip]` to skip the build and release process, `[release]` to trigger a release, or `[portfolio]` to trigger a release and make a pull request to the `portfolio` repo.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/PhantomOffKanagawa/resume-generator.git
cd resume-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
# Or manually:
pip install jinja2 pyyaml
# You also need a LaTeX distribution (MiKTeX, TeX Live, etc.)
```

### 3. Edit your resume data

Edit `resume.yaml` with your information.

### 4. Generate your PDF

```bash
python resume_to_pdf.py
```

Your resume will be generated as `resume.pdf` in the project root.

## ⚙️ GitHub Actions: Auto-Build & Release

This repo includes `.github/workflows/release-resume.yml` to:

- Build your PDF on every push to `main`
- Attach the PDF to a GitHub Release

**To enable:**
1. Push your repo to GitHub.
2. Make changes to `resume.yaml` or the template and push – your PDF will be built and released automatically!

## 🖋️ Customizing the Template

- Edit `resume_template.tex` to change the look and layout.
- Use Jinja2 syntax (`{{ variable }}`) to insert YAML data.

## 🛠️ Requirements

- Python 3.9+
- [Jinja2](https://pypi.org/project/Jinja2/)
- [PyYAML](https://pypi.org/project/PyYAML/)
- LaTeX distribution (MiKTeX, TeX Live, etc.)

## 🧪 Testing Locally with act

To test the GitHub Actions workflow locally and see the output PDF:

1. [Install `act`](https://github.com/nektos/act)
2. Run:
   ```bash
   act --bind
   ```
   The PDF will be generated in your local directory as resume.pdf.

## 🤝 Contributing

Pull requests and issues are welcome! Help improve the template, workflow, or add new features.

---

Made with ❤️ by [PhantomOffKanagawa](https://github.com/PhantomOffKanagawa)