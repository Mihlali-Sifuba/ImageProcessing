# Define the root directory for the project (make empty string if using relative path)
$projectRoot = "C:\Users\sivuy\Documents\ImageProcessing"

# Check if the root directory exists
if (-not (Test-Path $projectRoot)) {
    Write-Error "The specified root directory does not exist: $projectRoot"
    exit
}

# Create .gitkeep files in each directory
Get-ChildItem -Path $projectRoot -Directory -Recurse | ForEach-Object {
    $gitkeepFile = Join-Path -Path $_.FullName -ChildPath ".gitkeep"
    
    try {
        if (-not (Test-Path $gitkeepFile)) {
            New-Item -Path $gitkeepFile -ItemType File -Force | Out-Null
            Write-Output "Created .gitkeep in: $($_.FullName)"
        } else {
            Write-Output ".gitkeep already exists in: $($_.FullName)"
        }
    } catch {
        Write-Error "Failed to create .gitkeep in: $($_.FullName). Error: $($_.Exception.Message)"
    }
}
