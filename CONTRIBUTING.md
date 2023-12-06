# Contributing to the AssemblyAI Cookbook

## Introduction: What is the Cookbook for?

The AssemblyAI Cookbook is a practical resource for developers working with AssemblyAI's API. It offers code examples, guides, and tutorials to help understand and utilize the API more effectively. It's a go-to guide for tackling specific problems or broadening your skills.

Contributions are essential for keeping the Cookbook relevant and useful. Whether fixing a bug or adding a new example, your input makes a difference.

## Getting Started
- Create an [AssemblyAI account and obtain your API key](https://www.assemblyai.com/dashboard/signup) to start building and testing your cookbook.
- Set up your development environment with the necessary tools for Python or JavaScript.
	- Use [Google Colabs](https://colab.research.google.com/) for developing and testing Jupyter notebooks.
- Consider using an existing cookbook as a template for your submission.

## Contribution Guidelines
**Types of Contributions**: 
- Bug fixes
- Cookbook contributions

### Making a Bug Fix:
- Create a new branch (`git checkout -b <name>/fix/<description>`).
- Commit your changes (`git commit -am 'fix: <description>'`).
- Test your changes to ensure they fix the issue.
- Push to the branch (`git push origin <name>/fix/<description>`).
- Create a new Pull Request detailing the bug and how your change fixes it.

### Contributing a Cookbook:
- Replace your API key with `YOUR_API_KEY` and audio URLs with `YOUR_AUDIO_URL` in your cookbook.
- Create your `.ipynb` file, then upload it to the desired directory in the repo.
- Create a new branch (`<name>/<cookbookname>`) and start a new pull request.

#### Cookbook Guidelines:
- Cookbooks vary in complexity and length, ranging from straightforward ones like [this transcription example](core-transcription/transcribe.ipynb) to more intricate projects such as [Extracting Quotes with Timestamps Using LeMUR + Semantic Search](lemur/transcript-citations.ipynb).
- [Try to use our SDKs.](https://www.assemblyai.com/docs/getting-started/transcribe-an-audio-file#step-1-install-the-sdk)
- Generally, stick to one `.ipynb` file. For longer tutorials requiring multiple files, create a folder with a README.

## Review Process
Contributions are reviewed by AssemblyAI team members for quality and relevance.

## Contact and Support
For help or questions, contact us at support@assemblyai.com.
