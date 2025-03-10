export default function Contact() {
  return (
    <section id="contact" className="p-10 text-center">
      <h2 className="text-3xl font-bold text-yellow-400">Contact Me</h2>
      <p className="text-gray-400 mt-2">Let's connect!</p>
      <div className="mt-4">
        <a href="mailto:lucas@flucas.io" className="text-yellow-300 hover:text-yellow-500">📧 Email</a> | 
        <a href="https://www.linkedin.com/in/furlanflucas" className="text-yellow-300 hover:text-yellow-500 ml-3">🔗 LinkedIn</a>
      </div>
    </section>
  );
}
