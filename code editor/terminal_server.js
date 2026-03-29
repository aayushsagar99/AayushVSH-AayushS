const WebSocket = require('ws');
const pty = require('node-pty');
const os = require('os');

const wss = new WebSocket.Server({ port: 3000 });
const shell = os.platform() === 'win32' ? 'powershell.exe' : 'bash';

wss.on('connection', (ws) => {
    const ptyProcess = pty.spawn(shell, [], {
        name: 'xterm-color',
        cols: 80, rows: 24,
        cwd: process.env.HOME,
        env: process.env
    });

    ptyProcess.onData(data => ws.send(data));
    ws.on('message', msg => ptyProcess.write(msg));
});
// Function to Create a New File
function createNewFile() {
  const name = prompt("Enter filename (e.g., helper.py):");
  if (!name || files[name]) return alert("Invalid or existing name!");

  // 1. Add to virtual file system
  files[name] = ""; 
  
  // 2. Add to sidebar DOM
  const explorer = document.getElementById('explorer');
  const div = document.createElement('div');
  div.className = 'file-item';
  div.innerHTML = `📄 ${name}`;
  div.onclick = () => openFile(name);
  explorer.appendChild(div);
  
  openFile(name); // Switch to the new file immediately
}
 const fileSystem = {
  "src": {
    type: "folder",
    children: {
      "main.py": { type: "file", content: "print('Hello from src!')" },
      "utils": {
        type: "folder",
        children: {
          "helper.py": { type: "file", content: "def help(): pass" }
        }
      }
    }
  },
  "README.md": { type: "file", content: "# Project Readme" }
};
function renderExplorer(data, container, path = "") {
  for (const name in data) {
    const item = data[name];
    const fullPath = path ? `${path}/${name}` : name;
    const div = document.createElement('div');
    
    if (item.type === "folder") {
      div.innerHTML = `<div class="folder-title">📁 ${name}</div>`;
      const childrenContainer = document.createElement('div');
      childrenContainer.style.paddingLeft = "15px";
      childrenContainer.style.display = "none"; // Collapsed by default
      
      div.onclick = (e) => {
        e.stopPropagation();
        childrenContainer.style.display = childrenContainer.style.display === "none" ? "block" : "none";
      };
      
      renderExplorer(item.children, childrenContainer, fullPath);
      div.appendChild(childrenContainer);
    } else {
      div.className = "file-item";
      div.innerHTML = `📄 ${name}`;
      div.onclick = (e) => {
        e.stopPropagation();
        openFile(fullPath, item.content);
      };
    }
    container.appendChild(div);
  }
}

// Initial call
renderExplorer(fileSystem, document.getElementById('explorer'));
const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3001;
const PROJECT_DIR = path.join(__dirname, 'project_files');

// Create the project folder if it doesn't exist
if (!fs.existsSync(PROJECT_DIR)) fs.mkdirSync(PROJECT_DIR);

app.use(cors());
app.use(bodyParser.json());

// 1. GET: List all files for the sidebar
app.get('/files', (req, res) => {
    const files = fs.readdirSync(PROJECT_DIR);
    res.json(files);
});

// 2. GET: Read a specific file's content
app.get('/files/:name', (req, res) => {
    const filePath = path.join(PROJECT_DIR, req.params.name);
    const content = fs.readFileSync(filePath, 'utf8');
    res.send(content);
});

// 3. POST: Save changes to a file
app.post('/save', (req, res) => {
    const { name, content } = req.body;
    const filePath = path.join(PROJECT_DIR, name);
    fs.writeFileSync(filePath, content);
    res.send({ status: 'Saved!' });
});

app.listen(PORT, () => console.log(`Backend running at http://localhost:${PORT}`));
