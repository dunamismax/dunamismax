import Image from "next/image";

export default function PhotographyPage() {
  const photos = [
    { id: 1, src: "https://via.placeholder.com/600x400?text=Placeholder+Photo+1", alt: "Placeholder Photo 1" },
    { id: 2, src: "https://via.placeholder.com/600x400?text=Placeholder+Photo+2", alt: "Placeholder Photo 2" },
    { id: 3, src: "https://via.placeholder.com/600x400?text=Placeholder+Photo+3", alt: "Placeholder Photo 3" },
    { id: 4, src: "https://via.placeholder.com/600x400?text=Placeholder+Photo+4", alt: "Placeholder Photo 4" },
    { id: 5, src: "https://via.placeholder.com/600x400?text=Placeholder+Photo+5", alt: "Placeholder Photo 5" },
    { id: 6, src: "https://via.placeholder.com/600x400?text=Placeholder+Photo+6", alt: "Placeholder Photo 6" },
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