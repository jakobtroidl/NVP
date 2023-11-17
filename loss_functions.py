import torch

def image_mse(mask, model_output, gt):
    model_output = model_output.squeeze()
    gt = gt.squeeze()
    if mask is None:
        return {'img_loss': ((model_output- gt) ** 2).mean()}
    else:
        return {'img_loss': (mask * (model_output - gt) ** 2).mean()}
    
def image_l1(mask, model_output, gt):
    model_output = model_output.squeeze()
    gt = gt.squeeze()
    if mask is None:
        return {'img_loss': torch.abs(model_output - gt).mean()}
    else:
        return {'img_loss': (mask * torch.abs(model_output - gt)).mean()}

