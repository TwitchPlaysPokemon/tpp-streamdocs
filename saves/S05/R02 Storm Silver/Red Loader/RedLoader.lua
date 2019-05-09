-- RedLoader.lua
-- Overwrites Red's party with the party file of your choosing
-- Written by M4_Used_Rollout for TPP Storm Silver 2018

-- Edit the line below to pick a different party to import
partyFileToLoad = "aoooo.party"

-- If you'd like to dump your own party, replace nil in the line below with a filename
partyFileToDump = nil

function DumpParty(filename, addresses, partySourceAddrLabel)
    if not filename then
        print("Must provide filename to dump party.")
        return false
    end
    local address = addresses[partySourceAddrLabel or "PartyOffset"]
    if AddressHasParty(address) then
        local partyLength = GetPartyLength(address, addresses)
        local party = memory.readbyterange(address, partyLength)
        local file = io.open(filename, 'wb')
        file:write(TableToString(party))
        file:close()
        return true
    end
    return false
end

function LoadToParty(filename, addresses, partyDestinationAddrLabel)
    if not filename then
        print("Must provide filename to load party.")
        return false
    end
    local file = io.open(filename, 'rb')
    local success = false
	if file ~= nil then
        local address = addresses[partyDestinationAddrLabel or "EnemyOffset"]
        if AddressHasParty(address) then
            local partyLength = GetPartyLength(address, addresses)
            local party = file:read(partyLength)
            file:close()
            WriteByteRange(party, address)
            success = true
        end
    end
    return success
end

function LoadToEnemy(filename, addresses)  
	if LoadToParty(filename, addresses, "EnemyOffset") then
        print("Loaded " .. filename .. " to " .. DEC_HEX(addresses["EnemyOffset"]))
    else
        print("Could not load " .. filename)
    end
end

lastCheckedMap = 0
frameDelayBeforeWrite = 60 -- Makes sure the game is done writing the party before we try to overwrite
waitFrames = frameDelayBeforeWrite

function OverwriteEnemyOnMap(mapId, filename)
    local addresses = FindDataStructures()
    local curMap = addresses["MapID"]
    if lastCheckedMap ~= curMap then
        --if we changed map since last we checked...
        if mapId == curMap and AddressHasParty(addresses["EnemyOffset"]) then
            --and we are on the correct map, and are in a battle...
            waitFrames = waitFrames - 1
            if waitFrames < 0 then
                --save the last checked map so we don't keep overwriting the party
                lastCheckedMap = curMap
                waitFrames = frameDelayBeforeWrite
                LoadToEnemy(filename, addresses)
            end
        elseif mapId ~= curMap then
            --reset and wait until we're on the right map
            lastCheckedMap = curMap
            waitFrames = frameDelayBeforeWrite
        end
    end
end

function OverwriteRedsPartyHGSS()
    --The top of Mt. Silver is Map Id 465
    --There are no other battles here, so it's safe to overwrite any battle
    --We could do this on Trainer Id, but Map Id is all I have.
    OverwriteEnemyOnMap(465, partyFileToLoad)
end

function FindDataStructures()
	local data = {}
	local vCheck = memory.readdword(0x02FFFE0C)
	if vCheck == 0x454B5049 or vCheck == 0x45475049 then --HGSS
        local baseAddr = memory.readdword(0x02111880)
        if baseAddr ~= 0x00 then
            data['Gen'] = 4
            data['Game'] = "HGSS"
            --offsets from here: https://projectpokemon.org/docs/gen-4/hgss-save-structure-r76/
            baseAddr = baseAddr + 0x10
            data['MapID'] = memory.readword(baseAddr + 0x1234)

            -- Offsets from Pokemon gen 4 lua script by MKDasher
            local pokeBase = memory.readdword(0x0211186C)
            local enemyAddr = pokeBase + 0x37970
            -- the party reading function checks the two dwords before the party
            data["WildOffset"] = pokeBase + 0x38540 - 8
            data["PartnerOffset"] = memory.readdword(enemyAddr) + 0x1C70 + 0xA1C - 8
            data["Enemy2Offset"] = memory.readdword(enemyAddr) + 0x1C70 + 0x1438 - 8
            data["EnemyOffset"] = memory.readdword(enemyAddr) + 0x1C70 - 8
            data["PartyOffset"] = pokeBase + 0xD088 - 8
        end  
	end
	return data
end

--http://lua-users.org/lists/lua-l/2004-09/msg00054.html
function DEC_HEX(IN)
	local B,K,OUT,I,D=16,"0123456789ABCDEF","",0
	while IN>0 do
		I=I+1
		IN,D=math.floor(IN/B),math.mod(IN,B)+1
		OUT=string.sub(K,D,D)..OUT
	end
	return OUT
end

function AddressHasParty(address)
    return address and memory.readdword(address) > 0 and memory.readdword(address) <= 6 and memory.readdword(address + 4) <= memory.readdword(address)
end

function GetPokeBytes(addresses)
    return addresses['Gen'] == 4 and 236 or 220
end

function GetPartyLength(partyAddress, addresses) 
    return memory.readbyte(partyAddress + 4) * GetPokeBytes(addresses) + 8
end

function WriteByteRange(s, startAddr)
    if startAddr == nil then
        startAddr = 1
    end
    for i = 1, string.len(s) do
        memory.writebyte(startAddr - 1 + i, string.byte(s, i))
    end
end

function TableToString(t)
    local s = ""
    for i, v in ipairs(t) do
        s = s .. string.char(v)
    end
    return s
end

emu.registerafter(OverwriteRedsPartyHGSS)

if partyFileToDump then
    local addresses = FindDataStructures()
    if DumpParty(partyFileToDump, addresses, "PartyOffset") then
        print("Dumped party at " .. DEC_HEX(addresses["PartyOffset"]) .. " to " .. partyFileToDump .. ". Multiple attemps may be necessary to get a clean copy.")
    else 
        print ("Could not dump party to " .. partyFileToDump)
    end
end