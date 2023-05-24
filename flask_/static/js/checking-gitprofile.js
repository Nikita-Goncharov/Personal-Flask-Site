const projectOL = document.querySelector(".projects-list")

async function checkingNewRepositories() {

    let i = 0

    let response = await fetch("https://api.github.com/users/Nikita-Goncharov/repos", {
        method: "GET",
        headers: {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer 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",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    })
    if (response.ok) {
        let json = await response.json();
        projectOL.innerHTML = ""
        for (let repo of json) {

            i++;
            projectOL.innerHTML += `
            <li>
                <a href="${repo["svn_url"]}">${repo["name"]}
                    <span><span class="brackets">[</span> ${repo["language"]} <span class="brackets">]</span></span>
                </a>
            </li>
            `

            if (i === 5) {
                break;
            }
        }
    } else {
        console.error("Ошибка HTTP: " + response.status);
    }
}

(async () => checkingNewRepositories())()
setInterval(() => checkingNewRepositories(), 1000 * 60 * 60 * 72) // Every 3 days

