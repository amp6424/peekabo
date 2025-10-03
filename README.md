# 👀 peekabo

**peekabo** is a fun and simple **cross-platform system information tool**, inspired by [`neofetch`](https://github.com/dylanaraps/neofetch).  
It helps you quickly "peek" into your machine and fetch essential system details in a clean, modular format.  

Built to be **lightweight, modular, and open-source** – peekabo is the perfect starter tool for learning GitHub collaboration, contributing to open-source, and extending system utilities.

---

## 📸 Preview

```bash
$ peekabo

👀 peekabo: Peeking into your system...

OS: macOS 15.6.1
CPU: Apple M2
Memory: 8 GB
Disk Usage: 256 GB / 512 GB
Network: my-macbook (192.168.1.10)
```

---

## ✨ Features
- Detect Operating System & Version
- CPU Information
- Memory Usage
- Disk Usage
- Network Details (Hostname, IP)
- Modular design → easy to add more modules
- Cross-platform (Windows, macOS, Linux)

---

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/<your-org>/peekabo.git
cd peekabo
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the tool:
```bash
python main.py
```

---

## 📦 Coming Soon: PyPI Package

We’re working on publishing peekabo to PyPI for global use.  
Soon you’ll be able to:

```bash
pip install peekabo
peekabo
```

---

## 🛠️ Usage

Basic usage:
```bash
python main.py
```

Optional arguments (future roadmap):
```bash
python main.py --json     # Output in JSON format
python main.py --minimal  # Only show OS + CPU
```

---

## 📂 Project Structure

```
peekabo/
│── .github/                  # GitHub templates
│   ├── ISSUE_TEMPLATE/
│   │    ├── bug_report.md
│   │    └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
│
│── modules/                  # system info modules
│   ├── __init__.py
│   ├── os_info.py
│   ├── cpu_info.py
│   ├── memory_info.py
│   ├── disk_info.py
│   └── network_info.py
│
│── tests/                    # unit tests
│   ├── test_os_info.py
│   └── test_cpu_info.py
│
│── .gitignore
│── LICENSE
│── README.md
│── CONTRIBUTING.md
│── CODE_OF_CONDUCT.md
│── requirements.txt
│── setup.py
│── main.py
```

---

## 👨‍💻 Contributing

We ❤️ contributions! Whether it’s fixing a bug, improving docs, or adding new modules, your help is welcome.

1. Fork the project  
2. Create your feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add feature: XYZ'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request 🎉  

Please check out our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.  

---

## 🧪 Running Tests

We use [pytest](https://docs.pytest.org/) for testing.  

Run all tests:
```bash
pytest
```

---

## 📜 License

peekabo is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🌍 Community Guidelines

We want peekabo to be a friendly and inclusive project.  
Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

---

## 🔮 Roadmap

- [ ] Add JSON / YAML output  
- [ ] Add GPU information  
- [ ] Add battery information  
- [ ] Add CLI flags for selective info  
- [ ] Publish to PyPI  
- [ ] Docker support  

---

## ⭐ Acknowledgements

- Inspired by [neofetch](https://github.com/dylanaraps/neofetch)  
- Built with ❤️ by our team at **peekabo**  
- Thanks to all our future contributors!  

---

## 🏷️ Badges

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)  
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)  
![Build](https://img.shields.io/badge/build-passing-success)  

---
