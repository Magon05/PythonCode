import pymem

pm = pymem.Pymem('mb_warband.exe')
modules = list(pm.list_modules())
for module in pm.process_base:
    print(module.name)
#client = pymem.process.module_from_name(pm.process_handle, "steam.dll").lpBaseOfDll
#player = pm.read_int(client)
#print(client, "\n", player)

print(pymem.ressources.structure.SYSTEM_INFO)