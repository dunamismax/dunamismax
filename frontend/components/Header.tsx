import Link from "next/link";
import { FaTwitter, FaReddit, FaGithub } from "react-icons/fa";
import { MdEmail } from "react-icons/md";

const Header = () => {
  return (
    <header className="bg-gray-800 text-white p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">
          <Link href="/">dunamismax.com</Link>
        </h1>
        <nav className="flex items-center space-x-4">
          <ul className="flex space-x-4">
            <li>
              <Link href="/about" className="hover:text-gray-300">About Me</Link>
            </li>
            <li>
              <Link href="/blog" className="hover:text-gray-300">Blog</Link>
            </li>
            <li>
              <Link href="/photography" className="hover:text-gray-300">Photography</Link>
            </li>
            <li>
              <Link href="/developer" className="hover:text-gray-300">Developer</Link>
            </li>
          </ul>
          <div className="flex space-x-3 ml-4">
            <a href="https://twitter.com/dunamismax" target="_blank" rel="noopener noreferrer" className="hover:text-gray-300">
              <FaTwitter size={20} />
            </a>
            <a href="https://www.reddit.com/user/dunamismax" target="_blank" rel="noopener noreferrer" className="hover:text-gray-300">
              <FaReddit size={20} />
            </a>
            <a href="https://github.com/dunamismax" target="_blank" rel="noopener noreferrer" className="hover:text-gray-300">
              <FaGithub size={20} />
            </a>
            <a href="mailto:dunamismax@tutamail.com" className="hover:text-gray-300">
              <MdEmail size={20} />
            </a>
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;
