from awpy.parser import DemoParser

demo_parser = DemoParser(
    demofile = "/home/dion/Downloads/1-427ac40e-2d24-4d43-83c1-7d38da1e1069-1-1.dem",
    parse_rate = 128,
    parse_kill_frames= True
)

data = demo_parser.parse()

print(data.keys())