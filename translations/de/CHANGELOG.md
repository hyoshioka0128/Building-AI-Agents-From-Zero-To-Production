# Änderungsprotokoll

Alle bemerkenswerten Änderungen an **Building AI Agents from Zero to Production** sind hier dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dieser Kurs ist ein lebender Lehrplan und kein versioniertes Softwarepaket, daher sind die Einträge nach dem Datum gruppiert,
an dem eine Änderung eingespielt wurde, statt nach einer semantischen Versionsnummer.

## [Unveröffentlicht]

### Hinzugefügt
- **Repository-Hygiene für öffentliche Freigabe** — verbessertes `.gitignore` mit einem eigenen
  Abschnitt für Python / Notebooks / Secrets / Betriebssystem (env-Datei-Varianten, `.pytest_cache/`, `.mypy_cache/`,
  `.ruff_cache/`, `.ipynb_checkpoints/`, `*.egg-info/`), während jede `*.env.example`-
  Datei weiterhin nachverfolgt wird. Dieses `CHANGELOG.md`, eine `AGENTS.md`-Leitfaden für Mitwirkende/Agenten
  und Kursfähigkeitsdateien wurden hinzugefügt.

### Geändert
- Repository für öffentliche Freigabe vorbereitet: persönliche und Live-Umgebungs-Identifikatoren
  (Konto-, Projekt-, Ressourcen-Gruppen- und Identitätsnamen) aus veröffentlichten Dokumenten entfernt
  und den internen Modernisierungs-/Lückenanalyse-Bericht aus dem Repository ausgelagert
  (seine lernerorientierte Zusammenfassung befindet sich in diesem Änderungsprotokoll).

## [2026 Foundry Modernisierung]

Eine vollständige technische, terminologische und curriculare Erneuerung zur Angleichung des Kurses an die
**Microsoft Foundry 2026** Plattform. Details zur Code-Migration siehe `MIGRATION-GUIDE.md`.

### Hinzugefügt
- **Lektion 5 – Produktions-Hosting von Agenten** (`lesson-5-hosted-agents-production/`): Gehostete Agenten vs.
  Capability Hosts, eigenes Cosmos DB / Storage / AI Search, Speicher- und Thread-Persistenz,
  genehmigte Abläufe für gehostete MCPs und eine Governance-Checkliste.
- **Lektion 6 – Microsoft Toolbox** (`lesson-6-toolbox/`): Werkzeuge einmal definieren und zentral verwalten,
  plus ein ausführbares Beispiel zum Konsumieren (`toolbox_agent.py`), das über einen
  einzigen MCP-Endpunkt auf eine Toolbox zugreift.
- **Lektion 7 – Multi-Agent & A2A** (`lesson-7-multi-agent-a2a/`): Einen Agenten über das offene
  Agent-zu-Agent (A2A) Protokoll (`a2a_server.py`) bereitstellen und einen entfernten Agenten als Peer
  konsumieren (`a2a_client.py`). Live-Ende-zu-Ende validiert.
- **Aufgaben-Empfehlungs-Agent** (`lesson-2-agent-development/task-recommendation-agent.py`):
  implementiert Szenario 2 aus Lektion 1 mit dem GitHub Remote MCP Server als Werkzeug.
- **Vector-Store Setup Skript** (`setup_vector_store.py`): erstellt und füllt den Vector Store,
  auf den der Mitarbeiter-Such-Agent angewiesen ist (zuvor referenziert, aber fehlend).
- **CI Smoke + statisches Gate** (`.github/workflows/smoke-test-hosted-agent.yml`): Ein `static`-Job führt
  `py_compile` und markdown-link-check bei jedem PR/Push aus; ein `smoke`-Job führt die AI Smoke Test
  Aktion gegen einen bereitgestellten gehosteten Agenten aus (OIDC, `workflow_dispatch`).
- **Voraussetzungen und Einrichtungshinweise** wurden zu jeder Lektion und zum Root-README hinzugefügt
  (Python 3.12+, `az login`, Modellhinweise, Kosten & Aufräumen).
- **Neues Flaggschiff-Dokument**: `MIGRATION-GUIDE.md`.

### Geändert
- **Neubenennung**: *Azure AI Foundry* → **Microsoft Foundry** im gesamten Kurs.
- **SDK-Migration** zur aktuellen Microsoft Agent Framework Oberfläche — Samples verwenden nun
  `agent-framework` `1.2.0` mit `FoundryChatClient` und der **Responses API**, ersetzt die früheren
  Muster `AzureAIClient` / `AzureAIAgentClient` / `AzureOpenAIChatClient`.
- **Abhängigkeiten festgelegt**: `requirements.txt` setzt jetzt `agent-framework`, `agent-framework-foundry`
  und verwandte Pakete fest, anstatt ungebundene Vorabversionen zu installieren, was die Reproduzierbarkeit verbessert.
- **Umgebungsvariablen** werden über `deploy.py`, `agent.yaml`, `main.py` und
  `.env.example` Dateien hinweg vereinheitlicht.
- Architekturdiagramme im README und der Agent-/Szenarien-Katalog wurden umgeschrieben, um den ausgelieferten Code widerzuspiegeln.

### Behoben
- Korrigierter defekter Link im Root-README zu Lektion 4 (`lesson-4-agentdeployment`).
- Ausgearbeitetes zuvor leeres README der Lektion 3 (Bewertungen + Beobachtbarkeit).
- Ersetzt das veraltete `asyncio.get_event_loop().run_until_complete`-Muster im
  Lernempfehlungs-Agent.

### Abgekündigt / Entfernt
- Alle Verwendungen der eingestellten **GPT-4o / GPT-4.1** Modelle entfernt. Chat- und Bewertungssamples verwenden nun
  **gpt-5.1**; Coding-Samples nutzen **gpt-5-codex**.
- Dokumentiert, dass **GitHub Models** eingestellt wird (30. Juli 2026); der Kurs bedient alle Modelle
  über Microsoft Foundry und ist nicht von GitHub Models abhängig.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->