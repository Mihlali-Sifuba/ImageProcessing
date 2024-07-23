# Define the root directory for the project (relative path)
$projectRoot = ""

# Create .gitkeep files in each directory
Get-ChildItem -Path $projectRoot -Directory -Recurse | ForEach-Object {
    $gitkeepFile = Join-Path -Path $_.FullName -ChildPath ".gitkeep"
    if (-not (Test-Path $gitkeepFile)) {
        New-Item -Path $gitkeepFile -ItemType File -Force
    }
}