const url = 'https://youtube-v2.p.rapidapi.com/video/details?video_id=PuQFESk0BrA';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '523b5e0547msh45a8da8f040a180p1946d7jsnd3876d11faf8',
		'X-RapidAPI-Host': 'youtube-v2.p.rapidapi.com'
	}
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}