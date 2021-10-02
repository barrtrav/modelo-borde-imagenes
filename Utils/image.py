from skimage import io, filters
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte

class DigImage:
    def __init__(self, path, parent = None):
        self.child = []
        self.path = path
        self.widget = None
        self.parent = parent
        
        self.filename = path.split('/')[-1]
        self.array = img_as_ubyte(rgb2gray(io.imread(path)))

        self.width = len(self.array[0])
        self.height = len(self.array)
        
        self.SaveImage('.temp')

    @property
    def GetName(self):
        return self.filename.split('.')[0]
    
    @property
    def GetExtension(self):
        return self.filename.split(',')[-1]

    def AddChild(self, path):
        self.child.append(DigImage(path, self))
        return self.child[-1]
    
    def SaveImage(self, new_path):
        io.imsave(f'{new_path}/{self.filename}', self.array, check_contrast=False)
    
    def SaveGroupImage(self, new_path):
        io.imsave(f'{new_path}/{self.filename}', self.array, check_contrast=False)
        for image in self.child:
            image.SaveGroupImage(new_path)

    def EdgesFilter(self, edge):
        if edge.filter == 'Sobel':
            if edge.ftype == 'Simple':
                image = filters.sobel(self.array)
                name = f'{self.GetName}_edge-Ss'
            if edge.ftype == 'Horizontal':
                image = filters.sobel_h(self.array)
                name = f'{self.GetName}_edge-Sh'
            if edge.ftype == 'Vertical':
                image = filters.sobel_v(self.array)
                name = f'{self.GetName}_edge-Sv'

        if edge.filter == 'Scharr':
            if edge.ftype == 'Simple':
                image = filters.scharr(self.array)
                name = f'{self.GetName}_edge-Cs'
            if edge.ftype == 'Horizontal':
                image = filters.scharr_h(self.array)
                name = f'{self.GetName}_edge-Ch'
            if edge.ftype == 'Vertical':
                image = filters.scharr_v(self.array)
                name = f'{self.GetName}_edge-cv'

        if edge.filter == 'Prewitt':
            if edge.ftype == 'Simple':
                image = filters.prewitt(self.array)
                name = f'{self.GetName}_edge-Ps'
            if edge.ftype == 'Horizontal':
                image = filters.prewitt_h(self.array)
                name = f'{self.GetName}_edge-Ph'
            if edge.ftype == 'Vertical':
                image = filters.prewitt_v(self.array)
                name = f'{self.GetName}_edge-Pv'

        if edge.filter == 'Roberts':
            if edge.ftype == 'Simple':
                image = filters.roberts(self.array)
                name = f'{self.GetName}_edge-Rs'
            if edge.ftype == 'Positive':
                image = filters.roberts_pos_diag(self.array)
                name = f'{self.GetName}_edge-Rp'
            if edge.ftype == 'Negative':
                image = filters.roberts_neg_diag(self.array)
                name = f'{self.GetName}_edge-Rn'
        
        if edge.filter == 'Laplace':
            image = filters.laplace(self.array, edge.ksize)
            name = f'{self.GetName}_edge-Rs'

        if edge.filter == 'Farid':
            if edge.ftype == 'Simple':
                image = filters.farid(self.array)
                name = f'{self.GetName}_edge-Fs'
            if edge.ftype == 'Horizontal':
                image = filters.farid_h(self.array)
                name = f'{self.GetName}_edge-Fh'
            if edge.ftype == 'Vertical':
                image = filters.farid_v(self.array)
                name = f'{self.GetName}_edge-Fv'

        new_path = f'.temp/{name}.{self.GetExtension}'
        io.imsave(new_path, image, check_contrast=False)

        return self.AddChild(new_path)

    def GaussFilter(self, gauss):
        image = filters.gaussian(self.array, sigma=gauss.sigma, mode=gauss.mode, cval=gauss.scalar)
        name = f'{self.GetName}_G{gauss.mode[0]}({gauss.sigma})'

        new_path = f'.temp/{name}.{self.GetExtension}'
        io.imsave(new_path, image, check_contrast=False)

        return self.AddChild(new_path)