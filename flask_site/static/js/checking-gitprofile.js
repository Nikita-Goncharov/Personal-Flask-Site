import {GITHUBAPI_TOKEN, GITHUBAPI_URL} from './gitAPIToken.js'

const projectOL = document.querySelector(".projects-list")

async function checkingNewRepositories() {
    let response = await fetch(GITHUBAPI_URL, {
        method: "GET",
        headers: {
            "Accept": "application/vnd.github+json",
            "Authorization": `Bearer ${GITHUBAPI_TOKEN}`,
            "X-GitHub-Api-Version": "2022-11-28"
        }
    })
    if (response.ok) {
        let json = await response.json();
        projectOL.innerHTML = ""
        let i = 0
        for (let repo of json) {
            if (i === 5) {
                break;
            }

            projectOL.innerHTML += `
            <li>
                <a href="${repo["svn_url"]}">${repo["name"]}
                    <span><span class="brackets">[</span> ${repo["language"]} <span class="brackets">]</span></span>
                </a>
            </li>
            `
            i++;
        }
    } else {
        console.error("Error request to GitHub profile: " + response.status);
    }
}

checkingNewRepositories()
setInterval(() => checkingNewRepositories(), 1000 * 60 * 60 * 72) // Every 3 days

