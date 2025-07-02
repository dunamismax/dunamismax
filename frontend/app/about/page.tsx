import { FaTwitter, FaBluesky, FaReddit, FaDiscord, FaSignal } from 'react-icons/fa';

export default function AboutPage() {
  return (
    <section className="py-8">
      <h2 className="text-3xl font-bold mb-4">About Me</h2>
      <p className="text-lg mb-6">
        I am an IT Director at an X-Ray Company and do software development on the side for fun.
      </p>

      <h3 className="text-2xl font-bold mb-3">Social Connections</h3>
      <ul className="space-y-2">
        <li className="flex items-center">
          <FaTwitter className="mr-2" /> Twitter: <a href="https://twitter.com/dunamismax" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline ml-1">@dunamismax</a>
        </li>
        <li className="flex items-center">
          <FaBluesky className="mr-2" /> Bluesky: <a href="https://bsky.app/profile/dunamismax.bsky.social" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline ml-1">@dunamismax.bsky.social</a>
        </li>
        <li className="flex items-center">
          <FaReddit className="mr-2" /> Reddit: <a href="https://www.reddit.com/user/dunamismax" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline ml-1">u/dunamismax</a>
        </li>
        <li className="flex items-center">
          <FaDiscord className="mr-2" /> Discord: dunamismax
        </li>
        <li className="flex items-center">
          <FaSignal className="mr-2" /> Signal: dunamismax.66
        </li>
      </ul>
    </section>
  );
}
