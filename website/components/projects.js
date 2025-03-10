export default function Projects() {
  const projects = [
    { title: "Fraud Detection with Kafka", link: "https://github.com/furlanflucas/fraud-detection" },
    { title: "AWS Infrastructure with Terraform", link: "https://github.com/furlanflucas/aws-terraform" },
    { title: "MLOps Pipeline with Kubeflow", link: "https://github.com/furlanflucas/mlops-pipeline" }
  ];

  return (
    <section id="projects" className="p-10">
      <h2 className="text-3xl font-bold text-yellow-400">Projects</h2>
      <div className="mt-5 grid grid-cols-1 md:grid-cols-2 gap-5">
        {projects.map((project, index) => (
          <a key={index} href={project.link} className="p-5 bg-gray-800 rounded-lg hover:bg-gray-700">
            <h3 className="text-xl font-semibold">{project.title}</h3>
            <p className="text-gray-400 mt-2">View on GitHub →</p>
          </a>
        ))}
      </div>
    </section>
  );
}
