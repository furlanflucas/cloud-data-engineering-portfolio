export default function Navbar() {
  return (
    <nav className="p-5 bg-gray-800 text-white flex justify-between">
      <h1 className="text-2xl font-bold">Flucas.io</h1>
      <div>
        <a href="#projects" className="mx-4 hover:text-yellow-400">Projects</a>
        <a href="#contact" className="mx-4 hover:text-yellow-400">Contact</a>
      </div>
    </nav>
  );
}
