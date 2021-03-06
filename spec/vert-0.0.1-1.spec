package = "VirtualLua"

version = "0.0.1-1"

source = { url = "git://github.com/stonedcoder/Lua-venv.git"
         , tag = "v0.0.1"
         }

description = { summary = "Creates isolated development environment"
              , detailed = [[
                  Vert is a tool for building isolated development environments akin to
                  virtualenv in python. It handles compiling and install lua to a local
                  directory as well as setting up luarocks.
                ]]
              , maintainer = "Raunaq Verma <raunaq@cb.lk>"
              }

dependencies = { "lua == 5.1"
               , "luafilesystem"
               , "luasocket"
               }

build = { type = "builtin"
        , modules = { vert = "./src/vert.lua" 
                    , optimal = "./src/optimal.lua"
                    }
        , install = { bin = { vert = "src/vert.lua" } }
        }

