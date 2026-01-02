# The-first-project

## First implementation: RTSP + YOLOv8 connectivity test

The very first thing to implement is **"Can we pull RTSP video reliably and run a simple detector"**. If this fails, nothing else matters. This demo connects to an existing CCTV RTSP stream and runs YOLOv8 to detect dogs/cats, which proves:

- RTSP connectivity to real hospital cameras/NVR
- Real-time inference pipeline works end-to-end
- Basic detection reliability in your lighting/cage setup

### Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/rtsp_yolo_demo.py \
  --rtsp "rtsp://<id>:<pw>@<ip>:554/Streaming/Channels/102" \
  --view
```

Press `q` to quit the preview window.

### Recommended RTSP sub-stream patterns

- Hikvision sub stream: `rtsp://<id>:<pw>@<IP>:554/Streaming/Channels/102`
- Dahua sub stream: `rtsp://<id>:<pw>@<IP>:554/cam/realmonitor?channel=1&subtype=1`
- Generic ONVIF: `rtsp://<id>:<pw>@<IP>:554/live`

## Next steps after this works

1. Add automatic camera discovery with ONVIF.
2. Log event-based alerts (e.g., no animal detected for 5 seconds).
3. Attach pose estimation (DeepLabCut/SLEAP) and behavior classification.
