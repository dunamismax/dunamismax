<p align="center">
  <img src="c.png" alt="C Programming Logo" width="200" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=3071A4&center=true&vCenter=true&width=800&lines=C+Systems+Programmer;Pure+C+HTTP+Web+Server;HTMX+Dynamic+Capabilities;ARM64+Optimized+Performance;Security-First+Development" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://clang.llvm.org/"><img src="https://img.shields.io/badge/Clang-17+-blue.svg?logo=llvm" alt="Clang Version"></a>
  <a href="https://htmx.org/"><img src="https://img.shields.io/badge/HTMX-1.9.10+-orange.svg" alt="HTMX Support"></a>
  <a href="https://libsodium.gitbook.io/doc/"><img src="https://img.shields.io/badge/LibSodium-1.0.20+-green.svg" alt="LibSodium"></a>
  <a href="https://developer.apple.com/documentation/apple-silicon"><img src="https://img.shields.io/badge/ARM64-Apple_Silicon-black.svg?logo=apple" alt="ARM64 Apple Silicon"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
</p>

---

## About

C systems programmer specializing in **web servers**, **cryptographic software**, and **high-performance applications**. I build secure, efficient systems from scratch using modern C with ARM64 optimization and security-first design principles.

**Current Focus**: Pure C HTTP servers, HTMX integration, cryptographic protocols, and ultra-lightweight web architectures.

---

## Featured Project

### **[C Web Server](https://github.com/dunamismax/c-web-server)** - Pure C HTTP Server with HTMX

<p align="center">
  <a href="https://github.com/dunamismax/c-web-server">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=c-web-server&theme=dark&show_owner=true" alt="C Web Server Repository" />
  </a>
</p>

**Latest Release** - A from-scratch HTTP web server demonstrating the power of combining pure C with modern web technologies:

**Core Features:**

- **Pure C Implementation**: Zero dependencies except pthread, built from scratch
- **HTMX Integration**: Dynamic content without heavy JavaScript frameworks
- **Security Hardened**: Path traversal protection, input validation, HTML escaping
- **Multi-threaded**: Concurrent client handling with pthread architecture
- **ARM64 Optimized**: Apple Silicon-specific optimizations with LTO
- **Ultra-Lightweight**: Sub-millisecond response times, minimal memory footprint

**Quick Start:**

```bash
git clone https://github.com/dunamismax/c-web-server.git
cd c-web-server && make run
# Server available at http://localhost:8080
```

**Technical Highlights:**

- Custom HTTP/1.1 parser with security validation
- Built-in API endpoints for HTMX dynamic features
- Memory-safe string operations and bounds checking
- Cross-platform support (macOS, Linux, BSD)
- Professional build system with sanitizers and static analysis

---

## Additional Projects

<p align="center">
  <a href="https://github.com/dunamismax/c-chat">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=c-chat&theme=dark&show_owner=true" alt="C-Chat Repository" />
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/dunamismax/c-monorepo">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=c-monorepo&theme=dark&show_owner=true" alt="C-Monorepo Repository" />
  </a>
</p>

### **[C-Chat](https://github.com/dunamismax/c-chat)** - End-to-End Encrypted Command-Line Chat

Complete encrypted messaging system with zero-knowledge architecture:

- **End-to-End Encryption**: ChaCha20-Poly1305 via libsodium with forward secrecy
- **Multi-threaded TCP Server**: Handles 1000+ concurrent connections
- **Custom Binary Protocol**: Efficient real-time message delivery
- **Memory Safety**: Comprehensive buffer protection and secure memory clearing

### **[C-Monorepo](https://github.com/dunamismax/c-monorepo)** - ARM64 Optimized C Development Template

Professional C development template and educational resource:

- **ARM64 Build System**: Optimized Makefile with parallel builds
- **Multiple Applications**: Calculator, file utilities, games with modern C patterns
- **Comprehensive Testing**: Memory safety validation and automated CI/CD
- **Educational Value**: Best practices for secure C development

---

## 💻 Technical Expertise

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=c,cpp,html,css,js,linux,apple,git,github,vscode" />
  </a>
</p>

**Core Technologies:**

- **C11/C17** with security-focused practices
- **Web Technologies** (HTTP/1.1, HTMX, HTML5, CSS3)
- **Network Programming** (TCP/UDP, custom protocols)
- **Cryptography** (libsodium, secure protocols)
- **Multi-threading** (pthreads, concurrent systems)

**Specialized Areas:**

- Pure C web server development
- HTMX and lightweight web architecture
- Cryptographic protocol implementation
- ARM64 Apple Silicon optimization
- Security-hardened application development

---

## Development Philosophy

**Security First** → All code written with memory safety and comprehensive input validation  
**Performance Focused** → ARM64 optimizations and efficient, lightweight algorithms  
**Modern Web** → Combining pure C performance with HTMX for dynamic capabilities  
**Standards Compliant** → Modern C standards with cross-platform compatibility  
**Test Driven** → Comprehensive testing including security and performance validation

---

## Quick Start Guide

**Try the C Web Server (Recommended):**

```bash
# Clone and build
git clone https://github.com/dunamismax/c-web-server.git
cd c-web-server && make

# Start server
make run
# Visit http://localhost:8080 for HTMX demos

# Custom port
./build/release/bin/c-web-server 3000
```

**Explore C-Chat:**

```bash
# Build encrypted chat system
git clone https://github.com/dunamismax/c-chat.git
cd c-chat && make

# Start server (Terminal 1)
make run-server

# Register and chat (Terminal 2)
./build/release/bin/c-chat --register alice
./build/release/bin/c-chat --login alice
```

**Use C-Monorepo Template:**

```bash
# Use as GitHub template (recommended)
# Click "Use this template" on the repository page

# Or clone directly
git clone https://github.com/dunamismax/c-monorepo.git
cd c-monorepo && make && make test
```

---

## Current Work

- **Advanced Web Features**: Expanding HTMX integration with additional dynamic endpoints
- **Performance Optimization**: Sub-millisecond response times and memory efficiency improvements
- **Security Research**: Advanced input validation and attack surface reduction
- **Educational Content**: C web programming tutorials and best practices documentation

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

## ☕ Support My Work

If you find my C programming projects valuable, consider supporting continued development:

<p align="center">
  <a href="https://www.buymeacoffee.com/dunamismax" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" />
  </a>
</p>

---

## Connect With Me

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https://reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>

---

<p align="center">
  <strong>Building the Future with Pure C & Modern Web Technologies</strong><br>
  <sub>From ultra-lightweight HTTP servers to encrypted communication systems</sub>
</p>

---
