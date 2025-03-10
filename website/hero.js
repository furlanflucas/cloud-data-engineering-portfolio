import { motion } from "framer-motion";

export default function Hero() {
  return (
    <section className="flex flex-col items-center justify-center h-screen">
      <motion.h1 
        className="text-5xl font-bold"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
      >
        Hi, I'm Lucas Furlan 👋
      </motion.h1>
      <p className="text-xl text-gray-400 mt-2">Cloud Engineer | MLOps | DevOps</p>
      <a 
        href="#projects" 
        className="mt-6 px-6 py-2 bg-yellow-400 text-gray-900 font-semibold rounded-md hover:bg-yellow-300 transition">
        View My Work
      </a>
    </section>
  );
}
