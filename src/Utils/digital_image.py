import numpy as np
import math

from skimage import io, filters
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte

class DigitalImage:
    '''
    Clase encargada de aplicar los diferentes filtros y 
    formar la jerarquia entre las imagenes.
    '''
    def __init__(self, path, parent=None):
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
        '''
        Propiedad que devuelve el nombre del fichero.
        '''
        name, _ = self.filename.split('.')
        return name
    
    @property
    def GetExtension(self):
        '''
        Propiedad que devuelve la extension del fichero.
        '''
        extention = self.filename[-3:]
        return extention

    def AddChild(self, path):
        '''
        Agrega una subimagen a la jerarquia con el nombre especificado.
        '''
        self.child.append(DigitalImage(path, self))
        return self.child[-1]
    
    def SaveImage(self, new_path):
        '''
        Guarda una imagen con el nombre especificado.
        '''
        io.imsave(f'{new_path}/{self.filename}', self.array, check_contrast=False)
    
    def SaveGroupImage(self, new_path):
        '''
        Guarda un conjunto de imagenes a partir del nombre especificado.
        '''
        io.imsave(f'{new_path}/{self.filename}', self.array, check_contrast=False)
        for image in self.child:
            image.SaveGroupImage(new_path)

    def EdgesFilter(self, edge):
        '''
        Aplica a la imagen el filtro edge segun los parametros escogidos.
        '''
        if edge.filter == 'Sobel':
            if edge.ftype == 'Simple':
                image = filters.sobel(self.array)
                name = f'{self.GetName}-edge-sobel-simple'
            if edge.ftype == 'Horizontal':
                image = filters.sobel_h(self.array)
                name = f'{self.GetName}-edge-sobel-horizontal'
            if edge.ftype == 'Vertical':
                image = filters.sobel_v(self.array)
                name = f'{self.GetName}-edge-sobel-vertical'
        if edge.filter == 'Scharr':
            if edge.ftype == 'Simple':
                image = filters.scharr(elf.array)
                name = f'{self.GetName}-edge-scharr-simple'
            if edge.ftype == 'Horizontal':
                image = filters.scharr_h(self.array)
                name = f'{self.GetName}-edge-scharr-horizontal'
            if edge.ftype == 'Vertical':
                image = filters.scharr_v(self.array)
                name = f'{self.GetName}-edge-scharr-vertical'
        if edge.filter == 'Prewitt':
            if edge.ftype == 'Simple':
                image = filters.prewitt(self.array)
                name = f'{self.GetName}-edge-prewitt-simple'
            if edge.ftype == 'Horizontal':
                image = filters.prewitt_h(self.array)
                name = f'{self.GetName}-edge-prewitt-horizontal'
            if edge.ftype == 'Vertical':
                image = filters.prewitt_v(self.array)
                name = f'{self.GetName}-edge-prewitt-vertical'
        if edge.filter == 'Roberts':
            if edge.ftype == 'Simple':
                image = filters.roberts(self.array)
                name = f'{self.GetName}-edge-roberts-simple'
            if edge.ftype == 'Positive':
                image = filters.roberts_pos_diag(self.array)
                name = f'{self.GetName}-edge-roberts-positive'
            if edge.ftype == 'Negative':
                image = filters.roberts_neg_diag(self.array)
                name = f'{self.GetName}-edge-roberts-negative'
        if edge.filter == 'Laplace':
            image = filters.laplace(self.array, edge.ksize)
            name = f'{self.GetName}-edge-laplace'
        if edge.filter == 'Farid':
            if edge.ftype == 'Simple':
                image = filters.farid(self.array)
                name = f'{self.GetName}-edge-farid-simple'
            if edge.ftype == 'Horizontal':
                image = filters.farid_h(self.array)
                name = f'{self.GetName}-edge-farid-horizontal'
            if edge.ftype == 'Vertical':
                image = filters.farid_v(self.array)
                name = f'{self.GetName}-edge-farid-vertical'

        new_path = f'.temp/{name}.{self.GetExtension}'
        io.imsave(new_path, image, check_contrast=False)
        return self.AddChild(new_path)

    def GaussFilter(self, gauss):
        '''
        Aplica a la imagen el filtro gauss segun los parametros escogidos. 
        '''
        image = filters.gaussian(self.array, sigma=gauss.sigma, mode=gauss.mode, cval=gauss.scalar)
        name = f'{self.GetName}-gauss-{gauss.mode}-{gauss.sigma}'
        new_path = f'.temp/{name}.{self.GetExtension}'
        io.imsave(new_path, image, check_contrast=False)

        return self.AddChild(new_path)

    def ThresholdFilter(self, thresh):
        '''
        Aplica a la imagen el filtro threshold segun los parametros escogidos.
        '''
        if thresh.type == 'Local':
            image = filters.threshold_local(self.array, thresh.block_size, method=thresh.method, offset=thresh.offset, mode=thresh.mode, cval=thresh.scalar)
            name = f'{self.GetName}-threshold-local'
        if thresh.type == 'Niblack':
            image = filters.threshold_niblack(self.array, window_size=thresh.block_size, k=thresh.scalar)
            name = f'{self.GetName}-threshold-niblack'

        new_path = f'.temp/{name}.{self.GetExtension}'
        io.imsave(new_path, image, check_contrast=False)
        return self.AddChild(new_path)

    @property
    def QualityMeasures(self):
        if self.parent:
            mse = (np.square(self.parent.array - self.array)).mean()
            rmse = np.sqrt(mse)
            mu = np.sum(self.array)/(self.width * self.height)
            return rmse , 10*math.log10(255/mse), mu/np.std(self.parent.array)
        return 0, 0, 0
        