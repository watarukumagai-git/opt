#coding: utf-8 
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm
from matplotlib.colors import Normalize
plt.rcParams['font.family'] = 'Times New Roman'

from .get_eval import get_vio_class
from .get_eval import get_obj_class

class figure_save_class:
    def trend(self, figure_label, x, y, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        y_min = figure_label[2]
        y_max = figure_label[3]

        fig = plt.figure(figsize=(6,4))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)
        ax.plot(x, y, "C0", lw=0.5)
        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.tick_params(labelsize=12)
        #ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])

        plt.tick_params(labelsize=12, direction = "in")
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")


    def gbest_trend(self, figure_label, x, y1, y2, fig_file_name):
        x_label_name = figure_label[0]
        y1_label_name = figure_label[1]
        y2_label_name = figure_label[2]
        legend_name1 = figure_label[3]
        legend_name2 = figure_label[4]
        y1_min = figure_label[5]
        y1_max = figure_label[6]
        y2_min = figure_label[7]
        y2_max = figure_label[8]

        fig = plt.figure(figsize=(6,4))
        fig.patch.set_facecolor('white')
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot(x, y1, "C0", label=legend_name1, lw=0.5)
        ax1.set_xlabel(x_label_name, fontsize=16)
        ax1.set_ylabel(y1_label_name, fontsize=16)
        ax1.tick_params(labelsize=12)
        #ax.set_xlim([x_min, x_max])
        ax1.set_ylim([y1_min, y1_max])

        ax2 = ax1.twinx()
        ax2.plot(x, y2, "C1", label=legend_name2, lw=0.5)
        ax2.set_ylabel(y2_label_name, fontsize=16)
        ax2.set_ylim([y2_min, y2_max])


        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1+h2, l1+l2, loc='upper right')

        plt.tick_params(labelsize=12, direction = "in")
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")


    def gbest_trend_uplow_dis(self, figure_label, x, y1, y21, y22, y23, fig_file_name):
        x_label_name = figure_label[0]
        y1_label_name = figure_label[1]
        y2_label_name = figure_label[2]
        legend_name1 = figure_label[3]
        legend_name21 = figure_label[4]
        legend_name22 = figure_label[5]
        legend_name23 = figure_label[6]
        y1_min = figure_label[7]
        y1_max = figure_label[8]
        y2_min = figure_label[9]
        y2_max = figure_label[10]

        fig = plt.figure(figsize=(6,4))
        fig.patch.set_facecolor('white')
        ax1 = fig.add_subplot(1,1,1)
        ax1.plot(x, y1, "C0", label=legend_name1, lw=0.5)
        ax1.set_xlabel(x_label_name, fontsize=16)
        ax1.set_ylabel(y1_label_name, fontsize=16)
        ax1.tick_params(labelsize=12)
        #ax.set_xlim([x_min, x_max])
        ax1.set_ylim([y1_min, y1_max])

        ax2 = ax1.twinx()
        ax2.plot(x, y21, "C1", label=legend_name21, lw=0.5)
        ax2.plot(x, y22, "C2", label=legend_name22, lw=0.5)
        ax2.plot(x, y23, "C3", label=legend_name23, lw=0.5)
        ax2.set_ylabel(y2_label_name, fontsize=16)
        ax2.set_ylim([y2_min, y2_max])


        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1+h2, l1+l2, loc='upper right')

        plt.tick_params(labelsize=12, direction = "in")
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")



    def all_trend(self, figure_label, x, y1, y2, fig_file_name):
        x_label_name = figure_label[0]
        y1_label_name = figure_label[1]
        y2_label_name = figure_label[2]
        legend_name1 = figure_label[3]
        legend_name2 = figure_label[4]
        y1_min = figure_label[5]
        y1_max = figure_label[6]
        y2_min = figure_label[7]
        y2_max = figure_label[8]
        m = len(y1[0])

        handles = []
        labels = ["C0", "C1"]

        fig = plt.figure(figsize=(6,4))
        fig.patch.set_facecolor('white')
        ax1 = fig.add_subplot(1,1,1)
        for i in range(0, m):
            if i == 0:
                ax1.plot(x, y1[:, i], "C0", label=legend_name1, lw=0.5, marker="o", markeredgecolor="C0", markeredgewidth=0.5, markerfacecolor="None", markersize=5, linestyle='None')
            else:
                ax1.plot(x, y1[:, i], "C0", lw=0.5, marker="o", markeredgecolor="C0", markeredgewidth=0.5, markerfacecolor="None", markersize=5, linestyle='None')
        ax1.set_xlabel(x_label_name, fontsize=16)
        ax1.set_ylabel(y1_label_name, fontsize=16)
        ax1.tick_params(labelsize=12)
        #ax.set_xlim([x_min, x_max])
        ax1.set_ylim([y1_min, y1_max])

        ax2 = ax1.twinx()
        for i in range(0, m):
            if i == 0:
                ax2.plot(x, y2[:, i], "C1", label=legend_name2, lw=0.5, marker="o", markeredgecolor="C1", markeredgewidth=0.5, markerfacecolor="None", markersize=5, linestyle='None')
            else:
                ax2.plot(x, y2[:, i], "C1", lw=0.5, marker="o", markeredgecolor="C1", markeredgewidth=0.5, markerfacecolor="None", markersize=5, linestyle='None')
        ax2.set_ylabel(y2_label_name, fontsize=16)
        ax2.set_ylim([y2_min, y2_max])


        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax1.legend(h1+h2, l1+l2, loc='upper right')

        plt.tick_params(labelsize=12, direction = "in")
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")



    def scatter_solution_space_contour(self, figure_label, x1, x2, gbest, X, Y, obj_mesh_box, feas_mesh_box, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        label_name1 = figure_label[2]
        label_name2 = figure_label[3]
        x_min = figure_label[4]
        x_max = figure_label[5]
        y_min = figure_label[6]
        y_max = figure_label[7]

        cmax = np.max(obj_mesh_box) - 50
        cmin = np.min(obj_mesh_box)
        n_delta = 200
        levels_array = np.linspace(cmin, cmax, n_delta)


        fig = plt.figure(figsize=(5,5))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)

        # contour
        ax.contour(X, Y, obj_mesh_box, linestyles='dashdot', alpha=1.0, cmap='coolwarm', levels=levels_array, norm=Normalize(vmin=cmin, vmax=cmax), linewidths = 0.5)
        #for g in range(0, len(feas_mesh_box[:, 0, 0])):
        #    ax.contourf(X, Y, feas_mesh_box[g, :, :], alpha=0.4, cmap='Greys')
        ax.contourf(X, Y, feas_mesh_box, alpha=0.3, cmap='Greys')
 
        # scatter
        ax.scatter(x1, x2, color="C0", s=40, alpha=1.0, marker="o", label=label_name1)

        # gbest scatter
        ax.scatter(gbest[0], gbest[1], s=20, marker="s", edgecolor="C1", facecolor="None", label=label_name2)


        ax.legend(loc='upper right')

        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.tick_params(direction = "in")

        plt.tick_params(labelsize=12)
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")



    def scatter_solution_space(self, figure_label, x1, x2, gbest, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        label_name1 = figure_label[2]
        label_name2 = figure_label[3]
        x_min = figure_label[4]
        x_max = figure_label[5]
        y_min = figure_label[6]
        y_max = figure_label[7]


        fig = plt.figure(figsize=(5,5))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)
 
        # scatter
        ax.scatter(x1, x2, color="C0", s=40, alpha=1.0, marker="o", label=label_name1)

        # gbest scatter
        ax.scatter(gbest[0], gbest[1], s=20, marker="s", edgecolor="C1", facecolor="None", label=label_name2)


        ax.legend(loc='upper right')

        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.tick_params(direction = "in")

        plt.tick_params(labelsize=12)
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")
        
        
    def draw_arrow(self, ax, z, w):
        point = {
            'start': [z[0], z[1]],
            'end': [z[0]+w[0], z[1]+w[1]]
        }

        ax.annotate('', xy=point['end'], xytext=point['start'],
                    arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                    headlength=10, connectionstyle='arc3',
                                    facecolor='gray', edgecolor='gray')
                   )


    def scatter_contour(self, ax, minmax, x, fv_mesh_box, z, w, label_name):
        cmax = np.max(fv_mesh_box)
        cmin = np.min(fv_mesh_box)
        n_delta = 30
        levels_array = np.linspace(cmin, cmax, n_delta)

        # contour
        ax.contour(x[0,:,:], x[1,:,:], fv_mesh_box, linestyles='dashdot', alpha=1.0, cmap='coolwarm', levels=levels_array, norm=Normalize(vmin=cmin, vmax=cmax), linewidths = 1.0)
        
        # xi scatter
        #ax.scatter(x1, x2, color="C0", s=40, marker="o", label=label_name1)
        
        #xscale = np.max(fv_mesh_box)*0.75
        xscale = 1
        if w.ndim == 1:
            self.draw_arrow(ax, z, xscale*w)
        else:
            for i in range(0, len(w)):
                self.draw_arrow(ax, z, xscale*w[i])
        
        # ideal scatter
        ax.scatter(z[0], z[1], s=20, marker="s", edgecolor="C1", facecolor="white", label=label_name)
        return ax

    def scatter_obj_vio_space_contour(self, figure_label, minmax, x, fv_mesh_box, z, w, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        label_name1 = figure_label[2]
        x_min = minmax[0]
        x_max = minmax[1]
        y_min = minmax[2]
        y_max = minmax[3]


        fig = plt.figure(figsize=(5,5))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)

        self.scatter_contour(ax, minmax, x, fv_mesh_box, z, w, label_name1)
        
        ax.legend(loc='upper right')

        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.tick_params(direction = "in")

        plt.tick_params(labelsize=12)
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")


    def scatter_obj_vio_space_contour_pareto(self, figure_label, minmax, x, fv_mesh_box, p, z, w, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        label_name1 = figure_label[2]
        label_name2 = figure_label[3]
        x_min = minmax[0]
        x_max = minmax[1]
        y_min = minmax[2]
        y_max = minmax[3]


        fig = plt.figure(figsize=(5,5))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)

        self.scatter_contour(ax, minmax, x, fv_mesh_box, z, w, label_name1)
        
        # pareto scatter
        ax.scatter(p[:, 0], p[:, 1], color="C0", label=label_name2)
        
        ax.legend(loc='upper right')

        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.tick_params(direction = "in")

        plt.tick_params(labelsize=12)
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")

    def scatter_obj_vio_space(self, figure_label, x1, x2, gbest, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        label_name1 = figure_label[2]
        label_name2 = figure_label[3]
        x_min = figure_label[4]
        x_max = figure_label[5]
        y_min = figure_label[6]
        y_max = figure_label[7]


        fig = plt.figure(figsize=(5,5))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)

        # xi scatter
        ax.scatter(x1, x2, color="C0", s=40, marker="o", label=label_name1)

        # gbest scatter
        ax.scatter(gbest[0], gbest[1], s=20, marker="s", edgecolor="C1", facecolor="None", label=label_name2)
 
        ax.legend(loc='upper right')

        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.tick_params(direction = "in")

        plt.tick_params(labelsize=12)
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")



    def scatter(self, figure_label, x1, x2, fig_file_name):
        x_label_name = figure_label[0]
        y_label_name = figure_label[1]
        x_min = figure_label[2]
        x_max = figure_label[3]
        y_min = figure_label[4]
        y_max = figure_label[5]


        fig = plt.figure(figsize=(5,5))
        fig.patch.set_facecolor('white')
        ax = fig.add_subplot(1,1,1)
 
        ax.scatter(x1, x2, color="C0", s=40, marker="o")

        ax.set_xlabel(x_label_name, fontsize=16)
        ax.set_ylabel(y_label_name, fontsize=16)
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.tick_params(direction = "in")

        plt.tick_params(labelsize=12)
        plt.tight_layout()
        plt.savefig(fig_file_name, bbox_inches="tight")
