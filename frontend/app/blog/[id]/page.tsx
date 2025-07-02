interface BlogPost {
  id: number;
  title: string;
  content: string;
  created_at: string;
}

async function getBlogPost(id: string): Promise<BlogPost> {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/blog-posts/${id}`);

  if (!res.ok) {
    throw new Error("Failed to fetch blog post");
  }

  return res.json();
}

export default async function BlogPostPage({ params }: { params: { id: string } }) {
  const post = await getBlogPost(params.id);

  return (
    <section className="py-8">
      <h2 className="text-3xl font-bold mb-4">{post.title}</h2>
      <p className="text-gray-500 text-sm mb-4">{new Date(post.created_at).toLocaleDateString()}</p>
      <div className="prose lg:prose-xl">
        <p>{post.content}</p>
      </div>
    </section>
  );
}
