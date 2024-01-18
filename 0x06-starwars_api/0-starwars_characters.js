#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const getCharacterData = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      } else {
        reject(error, `Error fetching character data from ${characterUrl}`);
      }
    });
  });
};

const printCharacters = async () => {
  try {
    const movieData = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          resolve(JSON.parse(body));
        } else {
          reject(error, 'Error fetching movie data.');
        }
      });
    });

    const characterNames = await Promise.all(movieData.characters.map(getCharacterData));

    for (const name of characterNames) {
      console.log(name);
    }
  } catch (error) {
    console.error(error);
  }
};

printCharacters();
