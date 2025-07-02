export default function BlogPage() {
  const blogPosts = [
    {
      id: 1,
      title: "My First Blog Post",
      date: "July 1, 2025",
      excerpt: "This is the first placeholder blog post. Stay tuned for more content!",
    },
    {
      id: 2,
      title: "Another Exciting Post",
      date: "June 25, 2025",
      excerpt: "Here's another placeholder. I'll be sharing thoughts on tech, life, and everything in between.",
    },
    {
      id: 3,
      title: "A Third Placeholder",
      date: "June 20, 2025",
      excerpt: "Just a quick note to say hello. More substantial content coming soon!",
    },
  ];

  return (
    <section className="py-8">
      <h2 className="text-3xl font-bold mb-4">Blog</h2>
      <div className="space-y-8">
        {blogPosts.map((post) => (
          <article key={post.id} className="border-b pb-4">
            <h3 className="text-2xl font-bold mb-2">{post.title}</h3>
            <p className="text-gray-500 text-sm mb-2">{post.date}</p>
            <p className="text-lg">{post.excerpt}</p>
            <a href={`/blog/${post.id}`} className="text-blue-500 hover:underline">Read More</a>
          </article>
        ))}
      </div>
    </section>
  );
}
