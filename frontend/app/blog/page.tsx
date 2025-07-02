import Link from "next/link";

interface BlogPost {
  id: number;
  title: string;
  content: string;
  created_at: string;
}

async function getBlogPosts(): Promise<BlogPost[]> {
  // In a real application, you might want to use a more robust fetching library
  // and handle errors more gracefully.
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/blog-posts`, {
    cache: "no-store", // Ensure data is always fresh
  });

  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch blog posts");
  }

  return res.json();
}

export default async function BlogPage() {
  const blogPosts = await getBlogPosts();

  return (
    <section className="py-8">
      <h2 className="text-3xl font-bold mb-4">Blog</h2>
      <div className="space-y-8">
        {blogPosts.length === 0 ? (
          <p>No blog posts found. Please add some to your Supabase database.</p>
        ) : (
          blogPosts.map((post) => (
            <article key={post.id} className="border-b pb-4">
              <h3 className="text-2xl font-bold mb-2">{post.title}</h3>
              <p className="text-gray-500 text-sm mb-2">{new Date(post.created_at).toLocaleDateString()}</p>
              <p className="text-lg">{post.content.substring(0, 150)}...</p>
              <Link href={`/blog/${post.id}`} className="text-blue-500 hover:underline">Read More</Link>
            </article>
          ))
        )}
      </div>
    </section>
  );
}