import Image from "next/image";

export default function PhotographyPage() {
  const photos = [
    { id: 1, src: "/placeholder-photo-1.jpg", alt: "Placeholder Photo 1" },
    { id: 2, src: "/placeholder-photo-2.jpg", alt: "Placeholder Photo 2" },
    { id: 3, src: "/placeholder-photo-3.jpg", alt: "Placeholder Photo 3" },
    { id: 4, src: "/placeholder-photo-4.jpg", alt: "Placeholder Photo 4" },
    { id: 5, src: "/placeholder-photo-5.jpg", alt: "Placeholder Photo 5" },
    { id: 6, src: "/placeholder-photo-6.jpg", alt: "Placeholder Photo 6" },
  ];

  return (
    <section className="py-8">
      <h2 className="text-3xl font-bold mb-4">Photography Portfolio</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {photos.map((photo) => (
          <div key={photo.id} className="relative w-full h-64">
            <Image
              src={photo.src}
              alt={photo.alt}
              layout="fill"
              objectFit="cover"
              className="rounded-lg shadow-md"
            />
          </div>
        ))}
      </div>
    </section>
  );
}
