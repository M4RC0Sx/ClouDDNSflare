module.exports = {
    branches: ["master", "next"],
    plugins: [
        [
            "@semantic-release/commit-analyzer",
            {
                preset: "conventionalcommits",
                releaseRules: [
                    {
                        type: "refactor",
                        release: "patch",
                    },
                    {
                        type: "style",
                        release: "patch",
                    },
                    {
                        type: "ci",
                        release: "patch",
                    },
                    {
                        type: "build",
                        release: "patch",
                    },
                    {
                        type: "chore",
                        release: "patch",
                    },
                ],
            },
        ],
        [
            "@semantic-release/release-notes-generator",
            {
                preset: "conventionalcommits",
            },
        ],
        [
            "@semantic-release/changelog",
            {
                changelogTitle:
                    "# ClouDDNSflare\n\nAll notable changes to this project will be documented in this file. See\n[Conventional Commits](https://conventionalcommits.org) for commit guidelines.",
            },
        ],
        [
            "semantic-release-replace-plugin",
            {
                replacements: [
                    {
                        files: ["pyproject.toml"],
                        from: 'version = ".*"',
                        to: 'version = "${nextRelease.version}"',
                        countMatches: true,
                    },
                ],
            },
        ],
        [
            "@codedependant/semantic-release-docker",
            {
                dockerImage: "m4rc0sx/clouddnsflare",
                dockerRegistry: `${process.env.DOCKER_REGISTRY}`,
                dockerTags: ["latest", "{{version}}"],
                dockerAutoClean: false
            },
        ],
        [
            "@semantic-release/git",
            {
                message:
                    "chore: release ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
                assets: ["CHANGELOG.md", "pyproject.toml"],
            },
        ],
    ],
};