const CONFIGURATION = {
    "locations": [
      {"title":"14 Nte. 880","address1":"14 Nte. 880","address2":"Viña del Mar, Valparaíso, Chile","coords":{"lat":-33.01031040309309,"lng":-71.54660861838529},"placeId":"ChIJAVVd8cLdiZYRM66cNqWGFq4"}
    ],
    "mapOptions": {"center":{"lat":38.0,"lng":-100.0},"fullscreenControl":true,"mapTypeControl":false,"streetViewControl":false,"zoom":4,"zoomControl":true,"maxZoom":17,"mapId":""},
    "mapsApiKey": "AIzaSyAtP8fAVfhQx0j_1RAS_qk3d6RjEFRIGOc",
    "capabilities": {"input":false,"autocomplete":false,"directions":false,"distanceMatrix":false,"details":false,"actions":false}
  };

document.addEventListener('DOMContentLoaded', async () => {
    await customElements.whenDefined('gmpx-store-locator');
    const locator = document.querySelector('gmpx-store-locator');
    locator.configureFromQuickBuilder(CONFIGURATION);
  });
