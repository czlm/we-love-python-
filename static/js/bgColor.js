const bgColor = {
    id: 'bgColor',
    beforeDraw: ((chart, args, plugins) => {
      const { ctx, chartArea:{top, bottom, left, right, width, height} } = chart;

      ctx.save();
      ctx.fillStyle = plugins.backgroundColor || 'pink';
      ctx.fillRect(0, 0, width, height)
      ctx.restore();
    })
}
