# Demos run from this repo

- [Codespaces](#codespaces)
- [Database schema management](#database-schema-management)
- [GHAS code quality](#code-quality)
- [Dependabot](#dependabot)
- [Scrum](#scrum)

---

## Codespaces

This repo has a simple [devcontainer.json](.devcontainer/devcontainer.json) file.  It installs and configures some custom extensions in VS Code ([here](.devcontainer/devcontainer.json#L21-L41)), spins up all the containers defined in [`docker-compose.yml`](docker-compose.yml), and starts the Flask app.  Expose port 5000 publicly, then copy "Local Address" URL.  Send a repo webhook to that URL, appended by `/webhook`.  It'll look something like this `https://your-codespace-url-5000.githubpreview.dev/webhook`.  

![images/port-forwarding.png](images/port-forwarding.png)

Note how it populates the `test_webhook` table with the repo owner, repo name, and timestamp with the SQL query below.

```sql
SELECT * FROM test_webhook;
```

![images/db-query.png](images/db-query.png)

## Database schema management

This repo uses [FlywayDB](https://flywaydb.org/) to manage the database schema in git.  The schema and config files are all in the [sql](sql) directory.  Docker compose will run `flyway migrate` on the empty database, which is great for development and testing.  GitHub Actions will also apply all schema on an empty database on pull request to make sure that the proposed schema changes are valid.  That workflow is [here](.github/workflows/db.yml), and it will always print the logs in case it's needed for troubleshooting.

![images/flyway-logs.png](images/flyway-logs.png)

An example of it failing because of an invalid schema change is in this [pull request](https://github.com/octodemo/webhook-demo/pull/23).  Note how it's unable to merge because this is a required check.

## GitHub Advanced Security

Don't use this as your main demo for security stuff.  It's not supposed to replace more mature demos, only to highlight a couple things that have come up as edge cases where I didn't have an easy answer.  This is a really REALLY simple Flask app.

### Code quality

It has some "code smells" found through the `security-and-quality` query pack, visible in the Security dashboard.  It should find some unused imports and variables that are declared and not used.

### Dependabot

There's nothing much to see here other than a [pull request](https://github.com/octodemo/webhook-demo/pull/20) for an out of date dependency and an overview of the [security alerts](https://github.com/octodemo/webhook-demo/security/dependabot) for it.

## Scrum

There's some scrum-y things in this repo too.  The first is an [issue template](.github/ISSUE_TEMPLATE/scrum.md) and [workflow](.github/workflows/scrum.yml) that opens a weekly planning issue to run sprint planning.  The schedule can be changed as needed in the workflow.  The workflow is currently disabled because this is a demo repo and I don't want it to be annoying anyone.

Next is a pair of shiny project boards.  Both have a bit of automation built in to explore too. :)

1. The current kanban-style board is [here](https://github.com/octodemo/webhook-demo/projects/1)
2. The new beta board is [here](https://github.com/orgs/octodemo/projects/62)
