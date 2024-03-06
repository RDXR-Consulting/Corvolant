# Corvolant

ВСТАВИТЬ СЮДА ФОТО

ДЕВИЗ 

-----
 
<p align="center">
  <a href="#"><img src="https://img.shields.io/github/release/cossacklabs/acra.svg" alt="GitHub release"></a>
  <a href="#"><img src="https://coveralls.io/repos/github/radixiura/Meca-Go/badge.svg?branch=main" alt='Coverage Status' /></a>
  <a href="#"><img class="badge" tag="github.com/cossacklabs/acra" src="https://goreportcard.com/badge/github.com/cossacklabs/acra"></a>
  <a href="#"><img src='https://godoc.org/github.com/cossacklabs/acra?status.svg'  alt='godoc'/></a>
</p>

<br>

| [Meca Examples](#) | [Documentation](#) | [Installation](#) | [Feedback](#) |
| ---- | ---- | ---- | ---- |

## What is MECA Project?
Meca - is a simple program which allows you to read/write memories to a unity storage.

Meca includes [](https://www.infoq.com/articles/ale-software-architects/) memory storage for organizations and individual customers. 

<table><thead><tr><th>Perfect cases for using Meca</th>
<th>For this, who</th></tr></thead>
<tbody><tr><td>You want to read memories of random people</td>
<td rowspan=3><ul>
<li>Cares about own memory</li>
<li>Likes to read</li>
<li>SaaS</li>
</tr><tr><td>You want to leave your step in a history!</td>
</tr><tr><td>You like to be more intelligent</td>
</tr></tbody></table>

## How does MECA work?
Meca is based on a GO programming language, so it uses a concurrency and parallel paradigm and allows u to work faster than even! 

## Installation and launch
0) sudo apt install postgres
1) service postgres start
2) sudo passwd postgres (sir1)
3) su -l postgres
4) postgres$: psql
5) psql$: CREATE USER dreamer WITH password ‘carbon2’;
6) psql$: CREATE DATABASE mecadb;
7) psql$: CREATE TABLE users(
   id SERIAL PRIMARY KEY,
   login CHARACTER VARYING(30),
   password CHARACTER VARYING(30),
   rank INTEGER
   );
9) psql$: GRANT ALL PRIVILEGES ON DATABASE mecadb to dreamer;
10) psql$: \c mecadb
11) mecadb$: GRANT ALL ON users TO dreamer;

|---|

0) sudo apt install go 
1) On your terminal "git clone https://github.com/radixiura/MECA"
2) cd MECA
3) chmod +x start.sh
4) ./start.sh


Requirements: Any OS with installed Golang.

| ⚙️ [Run MECA Example Project](https://github.com/radixiura/MECA) ⚙️ |
|---|

## Contributing to us
If you’d like to contribute your code or provide any other kind of input to Meca, you’re very welcome. Your starting point for contributing [is here](#).


## Contacts
If you want to ask a technical question, feel free to raise an [Issue](https://github.com/radixiura/Meca-Go/issues) or write to [radix_iura@protonmail.com](mailto:radix_iura@protonmail.com).
