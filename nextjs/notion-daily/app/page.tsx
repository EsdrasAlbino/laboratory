import { getDatabase } from "@/lib/notion";


export default function Home({ finances }) {
  console.log("finances", finances);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        Testing
      </div>
    </main>
  )
}

export async function getStaticProps() {

  const database = await getDatabase();
  console.log("database", database);
  return {
    props: {
      finances: database,
    },
    revalidate: 60
  };
}
