# BlockBeats MCP Server

An MCP server that delivers blockchain news and in-depth articles from BlockBeats for AI agents.

[![Discord](https://img.shields.io/discord/1353556181251133481?cacheSeconds=3600)](https://discord.gg/aRnuu2eJ)
![GitHub License](https://img.shields.io/github/license/kukapay/blockbeats-mcp)
![Python Version](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)


## Features

- **Fast News Retrieval**: Fetch the latest blockchain fast news articles using the `get_latest_news` tool.
- **In-Depth Articles**: Access detailed blockchain articles with the `get_latest_articles` tool.
- **Multi-Language Support**: Supports English (`en`), Simplified Chinese (`cn`), and Traditional Chinese (`cht`).

## Installation

### Installing via Smithery

To install BlockBeats News for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@kukapay/blockbeats-mcp):

```bash
npx -y @smithery/cli install @kukapay/blockbeats-mcp --client claude
```

### Manual Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kukapay/blockbeats-mcp.git
   cd blockbeats-mcp
   ```

2. **Install Dependencies**:
   ```bash
   pip install mcp[cli] httpx
   ```

3. **Run the Server**:
   - For development mode (hot reload enabled):
     ```bash
     mcp dev main.py
     ```
   - For production use with Claude Desktop:
     ```bash
     mcp install main.py --name "BlockBeats News"
     ```
     
## Usage

The server provides two main tools:

### `get_latest_news`
Fetches the latest blockchain fast news articles from BlockBeats' `open-api/open-flash` endpoint.

**Parameters**:
- `size` (int): Number of articles per page (default: 5).
- `max_pages` (int): Maximum number of pages to fetch (default: 1).
- `type` (str): News type filter, e.g., `'push'` for important news (default: `'push'`).
- `lang` (str): Language of the news (`'en'` for English, `'cn'` for Simplified Chinese, `'cht'` for Traditional Chinese; default: `'en'`).

**Example**:
- **Input**: "Get me the 2 latest blockchain news articles in English from one page."
- **Output**:
  ```
  ID: 288909
  Title: Bitcoin Falls Below $75,000, 24-Hour Drop Widens to 5.75%
  Content: <p>BlockBeats News, April 9 – According to HTX market data, Bitcoin has fallen below $75,000, currently priced at $74,854, with a 24-hour drop widening to 5.75%.</p>
  Link: https://m.theblockbeats.info/flash/288909
  Created: 2025-04-09 15:26:29

  ID: 288908
  Title: Ethereum Drops Below $1,400, Down 9.36% in 24 Hours
  Content: <p>BlockBeats News, April 9 – Per HTX market data, Ethereum has fallen below $1,400, now at $1,398, with a 24-hour decline of 9.36%.</p>
  Link: https://m.theblockbeats.info/flash/288908
  Created: 2025-04-09 15:22:24
  ```

### `get_latest_articles`
Fetches in-depth blockchain articles from BlockBeats' `open-api/open-information` endpoint.

**Parameters**:
- `size` (int): Number of articles per page (default: 5).
- `max_pages` (int): Maximum number of pages to fetch (default: 1).
- `type` (str): Article type filter, e.g., `'push'` for important articles (default: `'push'`).
- `lang` (str): Language of the articles (`'en'` for English, `'cn'` for Simplified Chinese, `'cht'` for Traditional Chinese; default: `'en'`).

**Example**:
- **Input**: "Show me one in-depth blockchain article in English from the first page with push type."
- **Output**:
  ```
  Title: Solo Bitcoin Miners Are Winning More Blocks Lately—What Gives?
  Description: Using a $180 Bitaxe miner with a 1.2 TH/s hash rate, the daily chance of mining a block is just 0.00068390%.
  Content: <blockquote>Original Title: Solo Bitcoin Miners Are Winning More Blocks Lately—What Gives?</blockquote><blockquote>Author: Mat Di Salvo, Decrypt</blockquote><blockquote>Translated by: Lila, BlockBeats</blockquote><p><br></p><p>Last week, another solo Bitcoin miner successfully mined a block, earning a reward of 3.125 BTC, worth nearly $260,000 including transaction fees. This is just one of several recent wins for solo miners in recent months.</p><p><br></p><p>Was this miner just lucky? Is solo mining becoming more common? Can an average person with a basic miner and modest hash power take on the big mining firms?</p><p><br></p><p>The answers vary. While solo miners—here referring to individual enthusiasts or small, low-profile groups—have indeed been mining blocks more often recently, the increase is modest and unlikely to surge dramatically.</p><p><br></p><p><img src="https://image.theblockbeats.info/file_v6/20250408/e870c395-deef-48de-b133-0a5ea85053d5.png?x-oss-process=image/quality,q_50/format,webp" alt="" data-href="" style=""/></p><p><br></p><p>Scott Norris, CEO of solo mining firm Optiminer, put it bluntly: solo mining is still like “buying a lottery ticket.”</p><p><br></p>...
  Link: https://m.theblockbeats.info/news/57650
  Created: 2025-04-08 23:30:00
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
