# Brazilian General Elections Results

Hello there.
Welcome!

Here you'll find all the files from Brazil's 2022 General Elections.
The results were extracted from the TSE official website. Check it here: <a href="https://dadosabertos.tse.jus.br/dataset/resultados-2022" target="_blank">Tribunal Superior Eleitoral</a>

The goal here is to focus all the results in a single place, and, most importantly, share the code I used to do so.

I know it's not the most pythonian code as it is a little verbose and redundant, but... it works :)

Please, feel free to share contributions. PR's are welcome!


----------------------------

Some technical notes:
1. When calculating votes we consider: Valid votes, Null votes, Blank votes and Party votes. We do not consider technical Null votes.
2. Results by party share aggregate both Nulls and Blanks.
3. Some files were too large and had to be compressed into .gz files. You may decompress it with your regular unzip software
