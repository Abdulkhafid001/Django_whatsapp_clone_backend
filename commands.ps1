

function startapp {
}
function makemigrations {
}
function migrate {
}
function rundjangoshell {
}



function showmenu {
    Clear-Host
    Write-Host @"
==================== Project Management ====================
1: Start app
2: Make migrations
3: Migrate
4: Run Django Shell
Q: Quit
==========================================================
"@
}

while ($true) {
    showmenu
    $selection = Read-Host "Please make a selection"
    
    switch ($selection) {
        '1' { startapp }
        '2' { makemigrations }
        '3' { migrate }
        '4' { rundjangoshell }
        'Q' { exit }
        default { Write-Host "Invalid option" }
    }
    
    Write-Host "`nPress any key to continue..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}