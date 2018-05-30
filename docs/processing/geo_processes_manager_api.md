<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="../stylesheets/swagger-ui.css" >
<style>
html
{
    box-sizing: border-box;
    overflow: -moz-scrollbars-vertical;
    overflow-y: scroll;
}
*,
*:before,
*:after
{
    box-sizing: inherit;
}

body {
    margin:0;
    background: #fafafa;
}
</style>

<div id="swagger-ui"></div>

<script src="../scripts/swagger-ui-bundle.js"> </script>
<script src="../scripts/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {
  const ui = SwaggerUIBundle({
    url: "https://raw.githubusercontent.com/airbusgeo/playground-docs/master/api/api_geo_processes_manager_v1.0.yaml",
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })

  window.ui = ui
}
</script>
