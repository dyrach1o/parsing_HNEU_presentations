<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Content Parser</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        h1, h2, h3, h4 {
            color: #333;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 4px;
            overflow: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        ul {
            list-style-type: disc;
            margin: 10px 0;
            padding-left: 20px;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>

<h1>Web Content Parser</h1>

<p>A simple command-line tool to <strong>parse</strong>, <strong>copy</strong>, and <strong>save</strong> specific content from a webpage.</p>

<h2>Features</h2>
<ul>
    <li><strong>Parse Content</strong>: Extracts content from a specified section of a webpage.</li>
    <li><strong>Copy to Clipboard</strong>: Copies the extracted content to your clipboard.</li>
    <li><strong>Save to File</strong>: Saves the parsed content as a <code>.txt</code> file in a chosen directory.</li>
</ul>

<h2>Prerequisites</h2>
<p>Ensure you have <strong>Python 3.x</strong> installed and the required packages:</p>
<ul>
    <li><code>requests</code></li>
    <li><code>beautifulsoup4</code></li>
    <li><code>pyperclip</code></li>
</ul>
<p>To install these packages, use the following command:</p>
<pre><code>pip install requests beautifulsoup4 pyperclip</code></pre>

<h2>Usage</h2>
<ol>
    <li>Clone or download this repository.</li>
    <li>Open a terminal and navigate to the directory containing the script.</li>
    <li>Run the script:
        <pre><code>python script_name.py</code></pre>
    </li>
</ol>

<h3>Commands</h3>
<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>-p</code></td>
        <td>Prompts for a URL and parses the content from the specified section on the webpage.</td>
    </tr>
    <tr>
        <td><code>-cop</code></td>
        <td>Copies the parsed content to the clipboard. Requires that you’ve already used <code>-p</code>.</td>
    </tr>
    <tr>
        <td><code>-save</code></td>
        <td>Saves the parsed content to a text file. Requires that you’ve already used <code>-p</code>.</td>
    </tr>
    <tr>
        <td><code>-help</code></td>
        <td>Displays a list of available commands.</td>
    </tr>
    <tr>
        <td><code>-terminate</code></td>
        <td>Exits the script.</td>
    </tr>
</table>

<h2>Example Workflow</h2>
<ol>
    <li>Start the script by running it in the terminal.</li>
    <li>Enter <code>-p</code> to parse a webpage and enter the URL when prompted.</li>
    <li>After parsing, use <code>-cop</code> to copy the content or <code>-save</code> to save it.</li>
    <li>To exit, type <code>-terminate</code>.</li>
</ol>

<h2>Error Handling</h2>
<p>The script includes basic error handling:</p>
<ul>
    <li>If the URL cannot be reached or parsed, an error message will appear.</li>
    <li>If you attempt to copy or save content before parsing, the script will prompt you to parse first.</li>
</ul>

<h2>Future Improvements</h2>
<p>Possible future improvements could include:</p>
<ul>
    <li>Allowing users to specify custom HTML tags or classes to parse.</li>
    <li>Adding options for different output formats, such as JSON or CSV.</li>
    <li>Enhanced error handling for better robustness.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

</body>
</html>
