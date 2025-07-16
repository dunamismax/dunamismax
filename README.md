<p align="center">
  <img src="https://github.com/dunamismax/ruby-rails/blob/main/rails.png" alt="Ruby on Rails Logo" width="400" />
</p>

<p align="center">
  <a href="https://github.com/dunamismax">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=24&pause=1000&color=CC342D&center=true&vCenter=true&width=800&lines=Ruby+on+Rails+Developer+%26+Architect;Building+Scalable+Monorepo+Platforms;Full-Stack+Ruby+Applications;Modern+Rails+Development;API+Design+%26+Implementation;Dark+Mode+UI+Specialist;Production-Ready+Ruby+Code;Shared+Libraries+%26+Utilities;CLI+Tools+%26+Automation;Blog+%26+Portfolio+Development;Interactive+API+Playgrounds;Text+Analysis+%26+Processing;Secure+Password+Generation;File+Organization+Systems;Code+Statistics+%26+Analytics;Deployment+%26+DevOps+Scripts;Testing+%26+Quality+Assurance;Responsive+Web+Design;Educational+Ruby+Resources;Open+Source+Contributions;Ruby+Gems+Development;Rails+Best+Practices;Monorepo+Architecture;Developer+Productivity+Tools" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://www.ruby-lang.org/en/"><img src="https://img.shields.io/badge/Ruby-3.3.0+-red.svg?logo=ruby" alt="Ruby Version"></a>
  <a href="https://rubyonrails.org/"><img src="https://img.shields.io/badge/Rails-8.0.2+-red.svg?logo=rubyonrails" alt="Rails Version"></a>
  <a href="https://bundler.io/"><img src="https://img.shields.io/badge/Bundler-2.0+-blue.svg?logo=rubygems" alt="Bundler"></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite-3.0+-blue.svg?logo=sqlite" alt="SQLite"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License"></a>
</p>

---

## About

Ruby on Rails developer and architect passionate about **scalable monorepo platforms**, **full-stack web applications**, **API design**, and **developer productivity tools**. I create comprehensive Ruby applications and build efficient, maintainable systems using modern Rails with a focus on code reuse, dark mode interfaces, and production-ready architectures.

**Current Focus**: Ruby on Rails monorepo development, interactive API playgrounds, CLI automation tools, dark mode UI design, and scalable application architectures.

**Mission**: Building production-quality Ruby applications that demonstrate best practices in monorepo architecture, shared library development, and modern Rails patterns that enhance developer productivity and code maintainability.

---

## My Ruby Rails Projects

I specialize in building scalable Ruby on Rails applications and monorepo architectures. Here's my flagship project that demonstrates comprehensive Ruby and Rails development practices:

<p align="center">
  <a href="https://github.com/dunamismax/ruby-rails">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dunamismax&repo=ruby-rails&theme=dark&show_owner=true" alt="Ruby Rails Monorepo" />
  </a>
</p>

### **[Ruby-Rails Monorepo](https://github.com/dunamismax/ruby-rails)** - Complete Ruby & Rails Development Platform

**The definitive Ruby on Rails monorepo** - A comprehensive platform featuring multiple production-ready applications, shared libraries, CLI tools, and automated scripts. This repository demonstrates modern Ruby and Rails practices with a focus on scalability, maintainability, and developer productivity.

**Applications & Features**:

- **🌙 Dunamismax** - Dark-themed personal blog and portfolio website with responsive design
- **🔧 API Playground** - Interactive API testing environment with 6 utility endpoints
- **📝 Blog Generator** - CLI tool for creating blog posts with metadata and statistics
- **📁 File Organizer** - CLI tool for organizing files by type, date, and custom rules
- **📊 Code Stats** - CLI tool for analyzing code statistics across projects

**Infrastructure & Architecture**:

- **💎 Shared Utilities Gem** - Common libraries for string manipulation, date formatting, and API utilities
- **🔧 Development Scripts** - Bootstrap, testing, and deployment automation
- **🏗️ Monorepo Structure** - Scalable architecture for multiple applications and shared code
- **🌑 Dark Mode UI** - Modern, elegant dark themes across all applications
- **🔐 Security Focused** - Production-ready code with comprehensive input validation

**Technical Highlights**:

- **Modern Rails 8.0.2** with Ruby 3.3.0+ for cutting-edge features
- **Production-Quality Code** with comprehensive error handling and validation
- **Comprehensive Testing** with automated test runners and quality checks
- **Professional Documentation** with extensive guides and API references
- **Developer Productivity** with automated setup, linting, and deployment scripts

---

## Technical Expertise

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=ruby,rails,html,css,js,sqlite,git,github,vscode,linux" />
  </a>
</p>

**Core Technologies:**

- **Ruby 3.3.0+** with modern syntax and performance optimizations
- **Rails 8.0.2+** with cutting-edge features and best practices
- **Web Technologies** (HTML5, CSS3, JavaScript, Turbo, Stimulus)
- **Database Systems** (SQLite, PostgreSQL, Active Record)
- **Testing Frameworks** (RSpec, Capybara, FactoryBot)
- **Development Tools** (Bundler, RuboCop, Brakeman, Git hooks)

**Specialized Areas:**

- Ruby on Rails monorepo architecture and development
- API design and implementation with comprehensive documentation
- Dark mode UI/UX design and responsive web interfaces
- CLI tool development and automation scripting
- Shared library development and gem creation
- Security-focused development with input validation
- Developer productivity tools and workflow automation

---

## Development Philosophy

**Code Reusability** → Building shared libraries and utilities that enhance productivity across projects  
**Security Focused** → All applications built with comprehensive input validation and security best practices  
**User Experience** → Modern, responsive dark mode interfaces with intuitive navigation  
**Developer Productivity** → Automated scripts, testing, and deployment tools that streamline workflows  
**Standards Compliant** → Following Ruby Style Guide and Rails conventions for maintainable code  
**API-First Design** → Interactive API playgrounds and comprehensive documentation for all endpoints

---

## Quick Start Guide

Explore my Ruby Rails monorepo and get started with modern Rails development:

### **[Ruby-Rails Monorepo](https://github.com/dunamismax/ruby-rails)** - Complete Development Platform

```bash
# Clone the comprehensive monorepo
git clone https://github.com/dunamismax/ruby-rails.git
cd ruby-rails

# Bootstrap the entire monorepo
ruby scripts/development/bootstrap.rb

# Install dependencies
bundle install

# Set up the Rails applications
cd apps/dunamismax && bundle install && bundle exec rails db:create db:migrate
cd ../apiplayground && bundle install && bundle exec rails db:create db:migrate

# Start the applications
cd apps/dunamismax && bundle exec rails server
# Visit http://localhost:3000 for the blog/portfolio

cd apps/apiplayground && bundle exec rails server -p 3001
# Visit http://localhost:3001 for the API playground
```

### **CLI Tools Usage**

```bash
# Blog Generator - Create blog posts with metadata
./apps/blog_generator/bin/blog_generator new "My New Post" --tags ruby,rails

# File Organizer - Organize files by type or date
./apps/file_organizer/bin/file_organizer by_type /path/to/directory

# Code Stats - Analyze project statistics
./apps/code_stats/bin/code_stats analyze --format json
```

### **Development Scripts**

```bash
# Run all tests across applications
ruby scripts/development/test_runner.rb

# Deploy applications
ruby scripts/deployment/deploy.rb --app dunamismax

# Clean up temporary files
ruby scripts/maintenance/cleanup.rb
```

---

## Learning Path Recommendations

**For Ruby Beginners**
Start with [Ruby-Rails Monorepo](https://github.com/dunamismax/ruby-rails) → Explore the shared utilities gem → Study the CLI tools → Build your own Ruby applications

**For Rails Developers**
Examine the Rails applications (Dunamismax & API Playground) → Study the monorepo architecture → Learn shared library patterns → Implement your own Rails apps

**For API Developers**
Explore the API Playground application → Study the endpoint implementations → Test the interactive API interface → Build your own API tools

**For CLI Enthusiasts**
Study the CLI tools (Blog Generator, File Organizer, Code Stats) → Learn the Thor gem usage → Examine the shared utilities integration → Create your own CLI applications

**For DevOps Engineers**
Examine the development scripts → Study the deployment automation → Learn the testing frameworks → Implement your own automation tools

---

## Current Work

- **Ruby-Rails Monorepo Enhancement**: Expanding the monorepo with additional applications and improving the shared utilities library
- **API Playground Development**: Adding more utility endpoints and enhancing the interactive testing interface
- **CLI Tools Expansion**: Building additional command-line tools for developer productivity and automation
- **Dark Mode UI Refinement**: Perfecting the dark mode themes across all applications for optimal user experience
- **Documentation Improvement**: Creating comprehensive guides and tutorials for Ruby and Rails development patterns
- **Community Engagement**: Sharing Ruby and Rails best practices through open-source contributions and educational content

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dunamismax&show_icons=true&theme=dark&count_private=true" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dunamismax&layout=compact&theme=dark" alt="Top Languages" />
</p>

---

## ☕ Support My Work

If you find my Ruby on Rails projects and development tools valuable, consider supporting continued development:

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
  <strong>Building the Future with Ruby on Rails & Developer Excellence</strong><br>
  <sub>From comprehensive monorepo platforms to production-ready applications</sub>
</p>
