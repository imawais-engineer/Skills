---
name: deploy-and-document
description: Deployment and documentation preferences for AI-built apps. Use when preparing stable functional apps for VPS deployment, static Vercel deployment, GitHub push workflow, subdomain/DNS planning, reverse proxy setup, SSL, ports, environment files, release notes, setup docs, testing checklists, or deployment instructions.
---

# Deploy And Document

## Deployment Rule

Deploy only when the app is stable, functional, tested, and validated unless the user explicitly asks for an earlier preview deployment.

## Default Deployment Choices

- Use VPS deployment for full-stack apps unless requirements say otherwise.
- Use build, push to GitHub, and Vercel auto-deploy for completely static apps.
- Use client/project requirements over defaults.

## VPS Requirements

For VPS apps, prepare:

- Ask whether the VPS already hosts other apps. If the answer is unknown, inspect running services, occupied ports, Nginx/Caddy virtual hosts, existing certificates, and DNS records before changing deployment configuration.
- Dedicated port per app.
- Subdomain per full-stack app.
- DNS `A` record pointing the subdomain to the VPS IP.
- Reverse proxy config with Nginx or Caddy.
- SSL through Let's Encrypt/Certbot or equivalent.
- Process management through Docker Compose, PM2, systemd, or stack-appropriate tooling.
- Environment variable setup.
- Restart/update workflow.
- Logs and basic health checks.

## Shared VPS Subdomain Safety

When multiple apps share one VPS IP, do not treat DNS as the app router. DNS only maps each subdomain to the same server IP; Nginx/Caddy must route by hostname.

Before issuing or declaring HTTPS ready:

1. Confirm the intended FQDN, for example `app.example.com`.
2. Confirm whether other apps already run on the VPS and list their domains, ports, process managers, and reverse-proxy entries.
3. Choose a dedicated unused localhost port for the new app.
4. Create an explicit reverse-proxy virtual host for the exact subdomain.
5. Check for conflicting `server_name` values, wildcard hosts, default servers, and catch-all blocks.
6. Check public DNS from at least two resolvers, including `A` and `AAAA` records.
7. Verify HTTP with the intended `Host` header before requesting SSL.
8. Request SSL for the exact subdomain and verify HTTPS with SNI.
9. Add or confirm a safe default/catch-all behavior so unknown hostnames do not load another app by accident.
10. Validate that the target subdomain loads the correct app and that unrelated app domains still route correctly.

If the user must configure DNS manually, provide only the exact required record values, then continue with server-side setup once DNS resolves.

## Static Vercel Flow

For static apps:

1. Build locally.
2. Push to GitHub.
3. Deploy through Vercel.
4. Ensure future pushes update Vercel automatically.

## Documentation Requirements

Create or update:

- Roadmap
- Architecture notes
- Database schema notes
- API documentation
- `.env.example`
- Setup instructions
- Deployment instructions
- Testing checklist
- Changelog or release notes

## Release Check

Before final deployment instructions, confirm:

- Requirements are verified.
- Implementation is validated.
- Tests ran or any missing tests are disclosed.
- Real persistence is ready when required.
- Auth/security are present for stable release.
- Port, subdomain, DNS target, SSL approach, and process manager are specified for VPS apps.
- On shared VPS deployments, exact hostname routing, SNI certificate, and default-host behavior are verified so one app cannot accidentally load under another app's subdomain.
