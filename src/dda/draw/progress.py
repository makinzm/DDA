from typing import Dict, ValuesView, Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import datetime

from dda.draw.aim import draw_aim

def visualize_progress(
        start_date: datetime.date, total_pages: int, pages_per_day_goal:int, input_data: Dict[str, int], is_cumulative_sum:bool = False, buffer_days:int = 0, save_path: Optional[str] = None
    ) -> Optional[tuple[tuple[ValuesView[str], ValuesView[int]], tuple[list[datetime.date], list[int]]]]:
    dates: DatetimeIndex
    pages: list[int]
    aim_dates, aim_pages = draw_aim(start_date, total_pages, pages_per_day_goal, buffer_days = buffer_days)
    plot_summation_list: np.ndarray
    if is_cumulative_sum:
        plot_summation_list = total_pages - np.cumsum(list(input_data.values()))
    else:
        plot_summation_list = total_pages - np.array(list(input_data.values()))
    date_keys_actual: list[datetime.date] = [datetime.datetime.strptime(_date, "%Y-%m-%d").date() for _date in input_data.keys()]
    if save_path is not None:
        fig: Figure
        ax: Axes
        fig, ax = plt.subplots()
        ax.plot(aim_dates, aim_pages, 'r.', label='Aim')
        ax.plot(aim_dates, aim_pages, 'r-', alpha=0.5)
        ax.plot(date_keys_actual, plot_summation_list, 'b.', label='Progress')
        ax.plot(date_keys_actual, plot_summation_list, 'b-', alpha=0.5)
        ax.set_ylim(bottom=-1)
        ax.set_xlabel('Date')
        ax.set_ylabel('Pages Read')
        ax.set_title('Reading Progress')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.show()
    else:
        return (aim_dates, aim_pages), (date_keys_actual, plot_summation_list)

if __name__ == "__main__":
    save_file: str = "../../../tmp_files/progress.visualize_progress.png"
    save_file_not_cumulative: str = "../../../tmp_files/progress.visualize_progress.not_cumulative.png"

    def _create_dummy() -> Dict[str, int]:
        input_data: Dict[str, int] = {}

        today = datetime.date.today()
        for i in range(1, 11):
            date = today + datetime.timedelta(days=i)
            pages_read = i * 10
            input_data[str(date)] = pages_read

        return input_data
    
    input_data: Dict[str, int] = _create_dummy()
    print("="*10)
    print(input_data)
    print("="*10)

    _tmp = visualize_progress(datetime.date.today(), 590, 10, input_data)
    print(_tmp)
    visualize_progress(datetime.date.today(), 590, 10, input_data, buffer_days=2, is_cumulative_sum=True, save_path=save_file)
    visualize_progress(datetime.date.today(), 590, 10, input_data, buffer_days=2, is_cumulative_sum=False, save_path=save_file)
