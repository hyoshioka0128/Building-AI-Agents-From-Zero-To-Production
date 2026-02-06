# Lektion 2 Agentenentwicklung

Willkommen zur zweiten Lektion des Kurses "Aufbau von KI-Agenten von Null bis zur Produktion"!

In dieser Lektion werden wir behandeln:

- Die Werkzeuge zur Erstellung unserer KI-Agenten
  
- Einrichtungshinweise für unsere Entwicklungsressourcen

- Best Practices für die Entwicklung von KI-Agenten
  
- Code-Durchgang zur Erstellung unserer KI-Agenten
  
Beginnen wir mit einem Blick auf die Werkzeuge, die wir zur Erstellung unserer KI-Agenten verwenden werden.

## Werkzeuge und Einrichtungshinweise

### Microsoft Foundry

Für den Zugriff auf Large Language Models (LLMs) verwenden wir [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry). Die Nutzung von Foundry ist kostenpflichtig, also stellen Sie bitte sicher, dass Sie die Anweisungen zur Kontoeinrichtung befolgen, falls Sie noch keinen Zugang haben.

### OpenAI-Modelle

Die Beispielcode für Agenten in diesem Kurs sind so eingerichtet, dass sie OpenAI-Modelle über [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) verwenden.

Verwenden Sie diese Anleitung, um zu lernen, wie ein Modell mit Foundry bereitgestellt wird: [Bereitstellung von Microsoft Foundry-Modellen im Foundry-Portal](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Wählen Sie für diesen Kurs ein GPT-4.1- oder neueres Modell aus.

### Microsoft Agent Framework

Wie bereits erwähnt, verwenden wir das [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), um unsere KI-Agenten zu erstellen und zu orchestrieren.

Um das Microsoft Agent Framework und andere benötigte Pakete zu installieren, führen Sie folgenden Befehl im Stammverzeichnis dieses Projekts aus:

```bash
pip install -r requirements.txt
```

### Setup der .env-Variablen

Um die Beispielcodes in diesem Kurs auszuführen, müssen Sie eine `.env`-Datei im Stammverzeichnis dieses Projekts erstellen.

Zur Vereinfachung können Sie die bereitgestellte Datei `.env.example` kopieren:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->