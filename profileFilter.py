from PIL import Image

def profileFilter(image,fil,out):
    im = Image.open(image)
    im = im.resize((960,960)).convert("RGB")
    overlay = Image.open(fil)
    overlay = overlay.resize((960,960)).convert("RGB")
    final = Image.blend(im,overlay,0.3)
    final.save(out)


if __name__ == "__main__":
    import sys
    try:
        profileFilter(sys.argv[1],sys.argv[2],sys.argv[3])
    except:
        print "Usage: python profileFilter.py profile-image filter-image output"
        sys.exit(1)
