import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Projects from "../components/Projects";
import Contact from "../components/Contact";

export default function Home() {
  return (
    <div className="bg-gray-900 text-white min-h-screen">
      <Navbar />
      <Hero />
      <Projects />
      <Contact />
    </div>
  );
}
