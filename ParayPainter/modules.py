#define functions for later


############# - Returns a list of names the length of listcount. 
# read_db() # - User-specified 'count' is passed via paray_gen(). 
############# - Should never be a reason to change this, but a smarter naming system could replace it (extension idea)

def read_db(listcount):
    names = []
    selected = []
    nlist = os.getenv("NLIST")
    with open(nlist,'r') as csvfile:
        reader = csv.reader(csvfile,skipinitialspace=True)
        names = list(reader)
    random.shuffle(names)
    for x in range(listcount):
        selected.append(names.pop(x))
    return selected

################ - This runs the experimental vector exploration code. Something extra for fun.
#              # - No truncation control in the interface, can be modified here in the code.
# gen_factor() # - Hard-coded to run the paray-512px.pt model, other models may not be compatible
#              # - savename is a file name concat. from dirname+timestamped image name. factor should be path to factor.pt.
################ - vec and scale set with interface sliders, creates scalar that determines the direction to 'explore' in.

def gen_factor(savename,factor,vec,scale):
    device = "cuda"
    eigvec = torch.load(factor)["eigvec"].to(device)
    ckpt = torch.load(model)
    g = Generator(512, 512, 2, channel_multiplier=2).to(device)
    g.load_state_dict(ckpt["g_ema"], strict=False)

    trunc = g.mean_latent(4096)

    latent = torch.randn(1, 512, device=device)
    latent = g.get_latent(latent)
    scalar = scale * eigvec[:, vec].unsqueeze(0)

    img, _ = g(
            [latent - scalar],
            truncation=0.7,
            truncation_latent=trunc,
            input_is_latent=True,
        )
    utils.save_image(img,savename)

############### = Should work with no problems now, directions in the interface.
# paray_gen() # = Took some fiddling to make it work nicely with the model.
############### = Anything worth changing is in the interface.

def paray_gen(model,p_num,t_a,t_b,norm=True):
    """Usage: paray_gen(model is model path from setup,p_num is how many pictures will be created, t_a and t_b should be between 0.0 and 1.0,norm can be toggled)"""
    device = "cuda"
    g_ema = Generator(
        512, 512, 2, channel_multiplier=2
    ).to(device)
    model = torch.load(model)
    truncation = random.uniform(t_a,t_b)
    g_ema.load_state_dict(model["g_ema"])
    
    with torch.no_grad():
        mlatent = g_ema.mean_latent(4096)
        names = read_db(p_num)
        time = "./gen"+strftime("%Y-%d%b-%H%M-%S",localtime())+"/"
        os.mkdir(time)
        g_ema.eval()
        for i in tqdm(range(p_num)):
            zseed = torch.randn(1, 512, device=device)
            truncation = random.uniform(t_a,t_b)
            mlatent = g_ema.mean_latent(4096)
            name = str(names[i]).translate({ord('['): '', ord(']'): '', ord('\''): ''})
            sample, _ = g_ema([zseed], truncation=truncation, truncation_latent=mlatent)
            utils.save_image(
                sample,
                time+name+".png",
                normalize=norm,
                range= (-1, 1),
            )
        print("\nOperation complete. Generated {p_num!s} images and saved them to \"{time!s}\"".format(p_num=p_num, time=time))