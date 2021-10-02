from skimage import io
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte

class DigImage:
    def __init__(self, path):
        self.child = []
        self.path = path
        self.widget = None
        
        self.filename = path.split('/')[-1]
        self.array = img_as_ubyte(rgb2gray(io.imread(path)))

        self.width = len(self.array[0])
        self.height = len(self.array)
        
        self.SaveImage('.temp')

    @property
    def GetName(self):
        return self.filename[:-4]
    
    @property
    def GetExtension(self):
        return self.filename[-4:]

    def AddChild(self, path):
        self.child.append(DigImage(path))
        return self.child[-1]
    
    def SaveImage(self, new_path):
        io.imsave(f'{new_path}/{self.filename}', self.array, check_contrast=False)
    
    def SaveGroupImage(self, new_path):
        io.imsave(f'{new_path}/{self.filename}', self.array, check_contrast=False)
        for image in self.child:
            image.SaveGroupImage(new_path)