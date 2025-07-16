<p align="center">
  <img src="https://github.com/dunamismax/c-chat/blob/main/c-chat.png" alt="C-Chat Logo" width="200" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=3071A4&center=true&vCenter=true&width=800&lines=C+Systems+Programmer;End-to-End+Encrypted+Chat;ARM64+Optimized+Development;Security-First+C+Programming" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://clang.llvm.org/"><img src="https://img.shields.io/badge/Clang-17+-blue.svg?logo=llvm" alt="Clang Version"></a>
  <a href="https://libsodium.gitbook.io/doc/"><img src="https://img.shields.io/badge/LibSodium-1.0.20+-green.svg" alt="LibSodium"></a>
  <a href="https://developer.apple.com/documentation/apple-silicon"><img src="https://img.shields.io/badge/ARM64-Apple_Silicon-black.svg?logo=apple" alt="ARM64 Apple Silicon"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
</p>

---

## About

C systems programmer focused on **cryptographic software**, **network programming**, and **high-performance applications**. I build secure, efficient systems using modern C with ARM64 optimization and security-first design principles.

**Core Focus**: Cryptographic protocols, network systems, memory-safe C development, and performance optimization.

---

## Featured Projects

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

A complete encrypted messaging system built in pure C featuring:

- **End-to-End Encryption**: ChaCha20-Poly1305 via libsodium with forward secrecy
- **Multi-threaded TCP Server**: Handles 1000+ concurrent connections with real-time message relay
- **Zero-Knowledge Architecture**: Server never accesses plaintext messages or private keys
- **Custom Binary Protocol**: Efficient TCP-based protocol with comprehensive error handling
- **Memory Safety**: Comprehensive buffer protection and secure memory clearing
- **Cross-Platform**: Native support for macOS, Linux, and BSD systems

**Technical Highlights:**

- Curve25519 key exchange with Argon2 password encryption
- pthread-based server with rate limiting and DoS protection
- Real-time message delivery with offline message queuing
- Comprehensive test suite with network integration tests
- ARM64-optimized build system with LTO

### **[C-Monorepo](https://github.com/dunamismax/c-monorepo)** - ARM64 Optimized C Development Template

Professional C development template with multiple applications and libraries:

- **Build System**: ARM64-optimized Makefile with parallel builds and security hardening
- **Applications**: Calculator, file utilities, text processor with modern C patterns
- **Libraries**: Optimized data structures and mathematical utilities
- **Testing**: Comprehensive test suites with memory safety validation
- **Cross-Platform**: macOS and Linux compatibility with automated CI/CD

---

## Technical Expertise

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=c,cpp,linux,apple,git,github,vscode" />
  </a>
</p>

**Core Technologies:**

- **C11/C17** with security-focused practices
- **Network Programming** (TCP/UDP, custom protocols)
- **Cryptography** (libsodium, OpenSSL)
- **Multi-threading** (pthreads, synchronization)
- **Build Systems** (Make, CMake, cross-platform)

**Specialized Areas:**

- Cryptographic protocol implementation
- High-performance network servers
- Memory-safe C development
- ARM64 Apple Silicon optimization
- Security-hardened applications

---

## Development Philosophy

**Security First** → All code written with memory safety and input validation  
**Performance Focused** → ARM64 optimizations and efficient algorithms  
**Standards Compliant** → Modern C standards with cross-platform compatibility  
**Test Driven** → Comprehensive testing including security and performance validation

---

## Quick Start

**Try C-Chat:**

```bash
# Clone and build
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
# Click "Use this template" on the repository

# Or clone directly
git clone https://github.com/dunamismax/c-monorepo.git
cd c-monorepo && make && make test
```

---

## Current Work

- **Advanced Cryptographic Protocols**: Implementing additional security features for C-Chat
- **Performance Optimization**: ARM64-specific optimizations for high-throughput applications
- **Network Programming**: TCP/UDP server architectures and custom protocol development
- **Educational Content**: C programming best practices and security patterns

---

## Connect

<p align="center">
  <a href="https://twitter.com/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
  <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank"><img src="https://img.shields.io/badge/Bluesky-blue?style=for-the-badge&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="https://reddit.com/user/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?&style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://discord.com/users/dunamismax" target="_blank"><img src="https://img.shields.io/badge/Discord-dunamismax-7289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://signal.me/#p/+dunamismax.66" target="_blank"><img src="https://img.shields.io/badge/Signal-dunamismax.66-3A76F0.svg?style=for-the-badge&logo=signal&logoColor=white" alt="Signal"></a>
</p>

---

<p align="center">
  <strong>Secure Systems Programming with Modern C</strong><br>
  <sub>Building cryptographic software and high-performance applications</sub>
</p>
