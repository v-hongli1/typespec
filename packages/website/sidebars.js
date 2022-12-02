// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    {
      type: "category",
      label: "Introduction",
      items: [
        "introduction/introduction",
        "introduction/installation",
        "introduction/usage",
        "introduction/formatter",
        {
          type: "category",
          label: "Configuration",
          items: ["introduction/configuration/configuration", "introduction/configuration/tracing"],
        },
        "introduction/releases",
        "introduction/faq",
      ],
    },
    {
      type: "category",
      label: "Getting Started",
      items: ["getting-started/getting-started", "getting-started/cadl-for-openapi-dev"],
    },
    {
      type: "category",
      label: "Language Basics",
      items: [
        "language-basics/overview",
        "language-basics/imports",
        "language-basics/namespaces",
        "language-basics/decorators",
        "language-basics/scalars",
        "language-basics/models",
        "language-basics/operations",
        "language-basics/interfaces",
        "language-basics/templates",
        "language-basics/enums",
        "language-basics/unions",
        "language-basics/intersections",
        "language-basics/type-literals",
        "language-basics/aliases",
        "language-basics/type-relations",
      ],
    },
    {
      type: "category",
      label: "Cadl Standard Library",
      items: [
        "standard-library/built-in-types",
        "standard-library/built-in-decorators",
        "standard-library/projected-names",
        {
          type: "category",
          label: "Http And Rest",
          items: [
            "standard-library/rest/overview",
            "standard-library/rest/decorators",
            "standard-library/rest/operations",
            "standard-library/rest/authentication",
            "standard-library/rest/resource-routing",
          ],
        },
        "standard-library/openapi",
      ],
    },
    {
      type: "category",
      label: "Writing Cadl Libraries",
      items: [
        "extending-cadl/basics",
        "extending-cadl/create-decorators",
        "extending-cadl/linters",
        "extending-cadl/emitters",
        "extending-cadl/writing-scaffolding-template",
      ],
    },
    {
      type: "category",
      label: "Release Notes",
      collapsed: true,
      link: {
        type: "generated-index",
        title: "Release Notes",
        slug: "/release-notes",
      },
      items: [
        {
          type: "autogenerated",
          dirName: "release-notes",
        },
      ],
    },
  ],
};

module.exports = sidebars;